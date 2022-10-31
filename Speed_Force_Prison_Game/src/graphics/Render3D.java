package graphics;

import input.Player;
import levels.Block;
import levels.Level;
import main.Display;
import main.Game;

/** handles the pixel motion effects */
public class Render3D extends Render {
    public double[] zBuffer;
    public double[] zBufferWall;
    private double renderDistance = 2000; /* shadowing; larger the number, faster things get dark */
    private double forwardMovement, rightMovement, cosine, sine, up, walking;
    public static int arenaBorderSize = 100; /* max x and z directions */
    
    /** constructor for the Render3D class */
    public Render3D(int width, int height) {
        super(width, height);
        zBuffer = new double[width * height];
        zBufferWall = new double[width];
    }
        
    /** renders the floor and ceiling */
    public void arena(Game game) {
        for (int x = 0; x < width; x++) {
            zBufferWall[x] = 0;
        }
        
        /* floor and ceiling distances away from center */
        double floorPosition = 8;
        double ceilingPosition = 8;
        
        /* rotations */
        double rotation = Player.rotation;
        cosine = Math.cos(rotation);
        sine = Math.sin(rotation);
        
        /* movement */
        forwardMovement = Player.z;
        rightMovement =  Player.x;
        up = Player.y;
        walking = 0;
                       
        /* render effects */
        for (int y = 0; y < height; y++) {
            double ceiling = (double) (y - height / 2) / height;   
            double z = (floorPosition + up) / ceiling;
            
            /* forward/backward movement */ 
            if (Player.walk) { 
                walking = Math.sin(game.time / 6.0) * 0.4;
                z = (floorPosition + up + walking) / ceiling;
            }
            
            /* adjusts head bobbing amounts */
            if (Player.crouchWalk && Player.walk) {
                walking = Math.sin(game.time / 6.0) * 0.15;
                z = (floorPosition + up + walking) / ceiling;
            } else if (Player.runForward && Player.walk) {
                walking = Math.sin(game.time / 6.0) * 0.8;
                z = (floorPosition + up + walking) / ceiling;
            } 
            
            /* ensure floor and ceiling are moving in same direction */
            if (ceiling < 0) {
                z = (ceilingPosition - up) / -ceiling;
                
                if (Player.walk) {
                    z = (ceilingPosition - up - walking) / -ceiling;
                }
            }
                        
            for (int x = 0; x < width; x++) {
                double depth = (double) (x - width / 2) / height;
                depth *= z;
                double xx = depth * cosine + z * sine + rightMovement;
                double yy = z * cosine - depth * sine + forwardMovement;
                int xPix = (int) (xx + rightMovement);
                int yPix = (int) (yy + forwardMovement);
                zBuffer[x + y * width] = z;
                pixels[x + y * width] = Texture.floor.pixels[(xPix & 7) + (yPix & 7) * 50];
            }
        }
        
        /* generates map layout */
        Level level = game.level;        
        
        /* creates blocks */
        /* lower half of wall */ 
        for (int xBlock = -arenaBorderSize; xBlock <= arenaBorderSize; xBlock++) {
            for (int zBlock = -arenaBorderSize; zBlock <= arenaBorderSize; zBlock++) {
                Block block = level.create(xBlock + 1, zBlock + 1);
                Block eastSide = level.create(xBlock + 2, zBlock + 1);
                Block southSide = level.create(xBlock + 1, zBlock + 2);
               
                /* creates pillars */
                if (block.solid) {
                    if (!eastSide.solid) 
                        renderWall(xBlock + 1, xBlock + 1, zBlock, zBlock + 1, 0);
                    if (!southSide.solid) 
                        renderWall(xBlock + 1, xBlock, zBlock + 1, zBlock + 1, 0);
                } else {
                    if (eastSide.solid) 
                        renderWall(xBlock + 1, xBlock + 1, zBlock + 1, zBlock, 0);
                    if (southSide.solid) 
                        renderWall(xBlock, xBlock + 1, zBlock + 1, zBlock + 1, 0);
                }
            }
        }

        /* upper half of wall */ 
        double upperHalf = 0.5;
        
        for (int xBlock = -arenaBorderSize; xBlock <= arenaBorderSize; xBlock++) {
            for (int zBlock = -arenaBorderSize; zBlock <= arenaBorderSize; zBlock++) {
                Block block = level.create(xBlock + 1, zBlock + 1);
                Block eastSide = level.create(xBlock + 2, zBlock + 1);
                Block southSide = level.create(xBlock + 1, zBlock + 2);
               
                /* creates pillars */
                if (block.solid) {
                    if (!eastSide.solid) 
                        renderWall(xBlock + 1, xBlock + 1, zBlock, zBlock + 1, upperHalf);
                    if (!southSide.solid) 
                        renderWall(xBlock + 1, xBlock, zBlock + 1, zBlock + 1, upperHalf);
                } else {
                    if (eastSide.solid) 
                        renderWall(xBlock + 1, xBlock + 1, zBlock + 1, zBlock, upperHalf);
                    if (southSide.solid) 
                        renderWall(xBlock, xBlock + 1, zBlock + 1, zBlock + 1, upperHalf);
                }
            }
        }
        
        /* blurs */
        for (int xBlock = -arenaBorderSize; xBlock <= arenaBorderSize; xBlock++) {
            for (int zBlock = -arenaBorderSize; zBlock <= arenaBorderSize; zBlock++) {
                Block block = level.create(xBlock + 1, zBlock + 1);
                
                /* blur walking buffer */
                for (int s = 0; s < block.blurs.size(); s++) {
                    Blur blur = block.blurs.get(s);
                    renderBlurs(xBlock + blur.x, blur.y, zBlock + blur.z);
                }
            }
        }

        /* wall collision handling */
        if (Player.walk) {
            wallCollision(level);
            blurCollisoin(level);
        }
    }
        
    /** wall collision handling */
    private void wallCollision(Level level) {
        /* player movement direction indicators */
        boolean forwardIndicated = Player.forwardDirection;
        boolean backwardIndicated = Player.backwardDirection;
        boolean leftIndicated = Player.leftDirection;
        boolean rightIndicated = Player.rightDirection;
        
        /* player direction facing */
        boolean playerFacingNorth = Math.cos(Player.rotation) > 0;
        boolean playerFacingEast = Math.sin(Player.rotation) > 0;
        boolean playerFacingSouth = Math.cos(Player.rotation) <= 0;
        boolean playerFacingWest = Math.sin(Player.rotation) <= 0;
        
        arenaBorderWallCollisions(forwardIndicated, backwardIndicated, leftIndicated, rightIndicated,
                playerFacingNorth, playerFacingEast, playerFacingSouth, playerFacingWest);
        
        /* inner walls */
        if (Player.x > 5 && Player.z > 5 && Player.x < 445 && Player.z < 445) { /* inner wall locations */
            /* player block location */
            int gridLocationX = (int) Math.floor(Player.x / 4.55) + 1;
            int gridLocationZ = (int) Math.floor(Player.z / 4.55) + 1;
            
            /* player standing on grid index */
            int gridIndexPlayerLocation = gridLocationX + gridLocationZ * arenaBorderSize;
            
            /* grid location indices surrounding the players current location */
            int forwardBlockIndex = 0;
            int rightBlockIndex = 0;
            int backwardBlockIndex = 0;
            int leftBlockIndex = 0;
            int forwardLeftBlockIndex = 0;
            int forwardRightBlockIndex = 0;
            int backwardLeftBlockIndex = 0;
            int backwardRightBlockIndex = 0;
            
            if (playerFacingNorth) { /* if northern facing */
                forwardBlockIndex = gridIndexPlayerLocation + arenaBorderSize;
                rightBlockIndex = gridIndexPlayerLocation + 1;
                backwardBlockIndex = gridIndexPlayerLocation - arenaBorderSize;
                leftBlockIndex = gridIndexPlayerLocation - 1;
                forwardLeftBlockIndex = gridIndexPlayerLocation + arenaBorderSize - 1;
                forwardRightBlockIndex = gridIndexPlayerLocation + arenaBorderSize + 1;
            } else { /* if southern facing */
                forwardBlockIndex = gridIndexPlayerLocation - arenaBorderSize;
                rightBlockIndex = gridIndexPlayerLocation - 1;
                backwardBlockIndex = gridIndexPlayerLocation + arenaBorderSize;
                leftBlockIndex = gridIndexPlayerLocation + 1;
                forwardLeftBlockIndex = gridIndexPlayerLocation - arenaBorderSize + 1;
                forwardRightBlockIndex = gridIndexPlayerLocation - arenaBorderSize - 1;
            }
            
            /* forward movement indicated */
            if (forwardIndicated) {
                if (playerFacingNorth) { /* if player facing north */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) < 1.5) /* if future collision straight */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid  && (Player.x % 4.55) > 3) /* if future collision left */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) < 1.5) /* if future collision right */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[forwardLeftBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 < 2.5)) /* if future forward/left corner collision */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 > 2)) /* if future forward/right corner collision */
                        Player.forwardCollision = true;
                } else { /* else; facing south */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) > 3) /* if future collision straight */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid  && (Player.x % 4.55) < 1.5) /* if future collision left */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) > 3) /* if future collision right */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[forwardLeftBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 > 2.5)) /* if future forward/left corner collision */
                        Player.forwardCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 < 2.5)) /* if future forward/right corner collision */
                        Player.forwardCollision = true;
                }
            }
        
            /* right movement indicated */
            if (rightIndicated) {
                if (playerFacingNorth) { /* if player facing north */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) > 3) /* if future collision straight */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[backwardBlockIndex].solid  && (Player.x % 4.55) < 1.5) /* if future collision behind */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) > 3) /* if future collision right */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[backwardRightBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 > 2.5)) /* if future behind/right corner collision */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 > 2.5)) /* if future forward/right corner collision */
                        Player.rightCollision = true;
                } else { /* else; facing south */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) < 1.5) /* if future collision straight */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[backwardBlockIndex].solid  && (Player.x % 4.55) > 3) /* if future collision behind */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) < 1.5) /* if future collision right */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[backwardLeftBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 < 2.5)) /* if future behind/right corner collision */
                        Player.rightCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 < 2.5)) /* if future forward/right corner collision */
                        Player.rightCollision = true;
                }
            }
            
            /* backward movement indicated */
            if (backwardIndicated) {
                if (playerFacingNorth) { /* if player facing north */
                    if (level.arenaBlocks[backwardBlockIndex].solid && (Player.z % 4.55) > 3) /* if future collision behind */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid  && (Player.x % 4.55) < 1.5) /* if future collision left */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) > 3) /* if future collision right */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[backwardLeftBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 < 2.5)) /* if future backward/left corner collision */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[backwardRightBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 > 2.5)) /* if future backward/right corner collision */
                        Player.backwardCollision = true;
                } else { /* else; facing south */
                    if (level.arenaBlocks[backwardBlockIndex].solid && (Player.z % 4.55) > 3) /* if future collision behind */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid  && (Player.x % 4.55) > 3) /* if future collision left */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[rightBlockIndex].solid && (Player.x % 4.55) < 1.5) /* if future collision right */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[backwardLeftBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 > 2.5)) /* if future backward/left corner collision */
                        Player.backwardCollision = true;
                    if (level.arenaBlocks[backwardRightBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 < 2.5)) /* if future backward/right corner collision */
                        Player.backwardCollision = true;
                }
            }
            
            /* left movement indicated */
            if (leftIndicated) {
                if (playerFacingNorth) { /* if player facing north */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) > 3) /* if future collision straight */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[backwardBlockIndex].solid  && (Player.x % 4.55) < 1.5) /* if future collision behind */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid && (Player.x % 4.55) < 1.5) /* if future collision left */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[forwardLeftBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 < 2.5)) /* if future backward/left corner collision */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 < 2.5)) /* if future forward/left corner collision */
                        Player.leftCollision = true;
                } else { /* else; facing south */
                    if (level.arenaBlocks[forwardBlockIndex].solid && (Player.z % 4.55) < 1.5) /* if future collision straight */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[backwardBlockIndex].solid  && (Player.x % 4.55) > 3) /* if future collision behind */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[leftBlockIndex].solid && (Player.x % 4.55) > 3) /* if future collision left */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[forwardLeftBlockIndex].solid && (Player.z % 4.55 > 2.5) && (Player.x % 4.55 > 2.5)) /* if future backward/left corner collision */
                        Player.leftCollision = true;
                    if (level.arenaBlocks[forwardRightBlockIndex].solid && (Player.z % 4.55 < 2.5) && (Player.x % 4.55 > 2.5)) /* if future forward/left corner collision */
                        Player.leftCollision = true;
                }
            }        
        }
    }
    
    /** handles player collisions with the arena border walls */
    private void arenaBorderWallCollisions(boolean forwardIndicated, boolean backwardIndicated, boolean leftIndicated, boolean rightIndicated,
            boolean playerFacingNorth, boolean playerFacingEast, boolean playerFacingSouth, boolean playerFacingWest) {
        /* arena dimensions for player */
        int maxZ = 447;
        int maxX = 447;
        int minZ = -1;
        int minX = -1;
        
        /* northern border */        
        if (forwardIndicated && playerFacingNorth && (Player.z > maxZ)) /* forward movement indicated */
            Player.forwardCollision = true;
        if (leftIndicated && playerFacingEast && (Player.z > maxZ)) /* left movement indicated */ 
            Player.leftCollision = true;
        if (rightIndicated && playerFacingWest && (Player.z > maxZ)) /* right movement indicated */
            Player.rightCollision = true;
        if (backwardIndicated&& playerFacingSouth && (Player.z > maxZ)) /* backward movement indicated */
            Player.backwardCollision = true;
        
        /* southern border */
        if (forwardIndicated && playerFacingSouth && (Player.z < minZ)) /* forward movement indicated */
            Player.forwardCollision = true;
        if (leftIndicated && playerFacingWest && (Player.z < minZ)) /* left movement indicated */ 
            Player.leftCollision = true;
        if (rightIndicated && playerFacingEast && (Player.z < minZ)) /* right movement indicated */
            Player.rightCollision = true;
        if (backwardIndicated&& playerFacingNorth && (Player.z < minZ)) /* backward movement indicated */
            Player.backwardCollision = true;
        
        /* eastern border */
        if (forwardIndicated && playerFacingEast && (Player.x > maxX)) /* forward movement indicated */
            Player.forwardCollision = true;
        if (leftIndicated && playerFacingSouth && (Player.x > maxX)) /* left movement indicated */ 
            Player.leftCollision = true;
        if (rightIndicated && playerFacingNorth && (Player.x > maxX)) /* right movement indicated */
            Player.rightCollision = true;
        if (backwardIndicated&& playerFacingWest && (Player.x > maxX)) /* backward movement indicated */
            Player.backwardCollision = true;
        
        /* western border*/
        if (forwardIndicated && playerFacingWest && (Player.x < minX)) /* forward movement indicated */
            Player.forwardCollision = true;
        if (leftIndicated && playerFacingNorth && (Player.x < minX)) /* left movement indicated */ 
            Player.leftCollision = true;
        if (rightIndicated && playerFacingSouth && (Player.x < minX)) /* right movement indicated */
            Player.rightCollision = true;
        if (backwardIndicated&& playerFacingEast && (Player.x < minX)) /* backward movement indicated */
            Player.backwardCollision = true;
    }
    
    /** handles action when player collects a blur */
    private void blurCollisoin(Level level) {
        /* player block location */
        int gridLocationX = (int) Math.floor(Player.x / 4.55) + 1;
        int gridLocationZ = (int) Math.floor(Player.z / 4.55) + 1;
        
        /* player standing on grid index */
        int gridIndexPlayerLocation = gridLocationX + gridLocationZ * arenaBorderSize;
        
        /* status at player location */
        boolean standingOnBlur = level.arenaBlocks[gridIndexPlayerLocation].blurs.size() != 0;
        
        /* player standing on blur; collect */
        if (standingOnBlur) {
            level.arenaBlocks[gridIndexPlayerLocation].blurs.remove(0);
            Display.blurs--;
        } 
    }
    
    /** rendering Blurs */
    public void renderBlurs(double x, double y, double z) {
        /* has wall move with users head bobbing while moving */
        double upCorrect = -0.0625;
        double rightCorrect = 0.11;
        double forwardCorrect = 0.11;
        double walkCorrect = 0.0625;
        
        /* blur calculations */
        double xCalculate = ((x / 2) - (rightMovement * rightCorrect)) * 2;
        double yCalculate = ((y / 2) - (up * upCorrect))+ (walking * walkCorrect) * 2;
        double zCalculate = ((z / 2) - (forwardMovement * forwardCorrect)) * 2;
        
        double rotationX = xCalculate * cosine - zCalculate * sine;
        double rotationY = yCalculate;
        double rotationZ = zCalculate * cosine + xCalculate * sine;
        
        /* center of block */
        double xCenter = width / 2;
        double yCenter = height / 2;

        /* rotation values */
        double xPixel = rotationX / rotationZ * height + xCenter;
        double yPixel = rotationY / rotationZ * height + yCenter;
        
        /* relative location of blur */
        double xPixelLeft = xPixel - 80 / rotationZ; /* extends blur 80 pixels in width in the left direction */
        double xPixelRight = xPixel + 80 / rotationZ; /* extends blur 80 pixels in width in the right direction */       
        double yPixelLeft = yPixel - 150 / rotationZ; /* extends blur 150 pixels in height in the upward direction */
        double yPixelRight = yPixel + 40 / rotationZ; /* extends blur 40 pixels in height in the downward direction */
        
        /* casting to integers */
        int xPixelLeftInt = (int) xPixelLeft;
        int xPixelRightInt = (int) xPixelRight;
        int yPixelLeftInt = (int) yPixelLeft;
        int yPixelRightInt = (int) yPixelRight;
        
        /* clipping */
        if (xPixelLeftInt < 0) /* x left side */
            xPixelLeftInt = 0;
        if (xPixelRightInt > width) /* x right side */
            xPixelRightInt = width;
        if (yPixelLeftInt < 0) /* y left side */
            yPixelLeftInt = 0;
        if (yPixelRightInt > height) /* y right side */
            yPixelRightInt = height;
        
        rotationZ *= 2; /* blur z positioning adjustment */ 
        
        /* render Blurs */
        for (int yPix = yPixelLeftInt; yPix < yPixelRightInt; yPix++) {
            for (int xPix = xPixelLeftInt; xPix < xPixelRightInt; xPix++) {
                if (zBuffer[xPix + yPix * width] > rotationZ) {
                    pixels[xPix + yPix * width] = Texture.blur.pixels[(xPix & 7) + (yPix & 7) * 30]; /* texture of blurs */
                    zBuffer[xPix + yPix * width] = rotationZ;
                }
            }
        }
    }
    
    /** render the walls */
    public void renderWall(double xLeft, double xRight, double zDistanceLeft, double zDistanceRight, double yHeight) {
        /* has wall move with users head bobbing while moving */
        double upCorrect = 0.0625;
        double rightCorrect = 0.11;
        double forwardCorrect = 0.11;
        double walkCorrect = -0.0625;
        
        /* left side of the wall */
        double xCalculateLeft = ((xLeft / 2) - (rightMovement * rightCorrect)) * 2;
        double zCalculateLeft = ((zDistanceLeft / 2) - (forwardMovement * forwardCorrect)) * 2;
        double rotationLeftSideX = xCalculateLeft * cosine - zCalculateLeft * sine;
        double yCornerTopLeft = (-yHeight - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double yCornerBottomLeft = ((+0.5 - yHeight) - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double rotationLeftSideZ = zCalculateLeft * cosine + xCalculateLeft * sine;
        
        /* right side of the wall */
        double xCalculateRight = ((xRight / 2) - (rightMovement * rightCorrect)) * 2;
        double zCalculateRight = ((zDistanceRight / 2) - (forwardMovement * forwardCorrect)) * 2;
        double rotationRightSideX = xCalculateRight * cosine - zCalculateRight * sine;
        double yCornerTopRight = (-yHeight - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double yCornerBottomRight = ((+0.5 - yHeight) - (-up * upCorrect + (walking * walkCorrect))) * 2;
        double rotationRightSideZ = zCalculateRight * cosine + xCalculateRight * sine;
        
        /* clipping */
        double texture3b = 0;
        double texture4b = 8;
        double clip = 0.5;
        
        if (rotationLeftSideZ < clip && rotationRightSideZ < clip) {
            return;
        }
        
        /* left side of the wall clipping */
        if (rotationLeftSideZ < clip) {
            double clip0 = (clip - rotationLeftSideZ) / (rotationRightSideZ - rotationLeftSideZ);
            rotationLeftSideZ = rotationLeftSideZ + (rotationRightSideZ - rotationLeftSideZ) * clip0;
            rotationLeftSideX = rotationLeftSideX + (rotationRightSideX - rotationLeftSideX) * clip0;
            texture3b = texture3b + (texture4b - texture3b) * clip0;
        }
        
        /* right side of the wall clipping */
        if (rotationRightSideZ < clip) {
            double clip0 = (clip - rotationLeftSideZ) / (rotationRightSideZ - rotationLeftSideZ);
            rotationRightSideZ = rotationLeftSideZ + (rotationRightSideZ - rotationLeftSideZ) * clip0;
            rotationRightSideX = rotationLeftSideX + (rotationRightSideX - rotationLeftSideX) * clip0;
            texture4b = texture3b + (texture4b - texture3b) * clip0;
        }
        
        /* pixel locations for walls */
        double xPixelLeft = (rotationLeftSideX / rotationLeftSideZ * height + width / 2);
        double xPixelRight = (rotationRightSideX / rotationRightSideZ * height + width / 2);
        
        /* skip rendering negative pixels */
        if (xPixelLeft >= xPixelRight) {
            return;
        }
        
        int xPixelLeftInt = (int) xPixelLeft;
        int xPixelRightInt = (int) xPixelRight;
        
        /* skip rendering pixels off screen */
        if (xPixelLeftInt < 0) {
            xPixelLeftInt = 0;
        } 
        
        if (xPixelRightInt > width) {
            xPixelRightInt = width;
        }
        
        /* four corner pins */
        double yPixelLeftTop = yCornerTopLeft / rotationLeftSideZ * height + height / 2.0;
        double yPixelLeftBottom = yCornerBottomLeft / rotationLeftSideZ * height + height / 2.0;
        double yPixelRightTop = yCornerTopRight / rotationRightSideZ * height + height / 2.0;
        double yPixelRightBottom = yCornerBottomRight / rotationRightSideZ * height + height / 2.0;

        /* texture preparation */
        double texture1 = 1 / rotationLeftSideZ;
        double texture2 = 1 / rotationRightSideZ;
        double texture3 = texture3b / rotationLeftSideZ;
        double texture4 = texture4b / rotationRightSideZ - texture3;
        
        /* render walls */
        for (int x = xPixelLeftInt; x < xPixelRightInt; x++) {
            double pixelRotation = (x - xPixelLeft) / (xPixelRight - xPixelLeft);          
            double zWall = texture1 + (texture2 - texture1) * pixelRotation;
            
            if (zBufferWall[x] > zWall) {
                continue;
            }
            
            zBufferWall[x] = zWall;
                        
            double yPixelTop = yPixelLeftTop + (yPixelRightTop - yPixelLeftTop) * pixelRotation;          
            double yPixelBottom = yPixelLeftBottom + (yPixelRightBottom - yPixelLeftBottom) * pixelRotation;            
            int yPixelTopInt = (int) yPixelTop;
            int yPixelBottomInt = (int) yPixelBottom;
            
            /* skip rendering pixels off screen */
            if (yPixelTopInt < 0) {
                yPixelTopInt = 0;
            }
            
            if (yPixelBottomInt > height) {
                yPixelBottomInt = height;
            }
            
            int xTexture = (int) ((texture3 + texture4 * pixelRotation) / zWall);

            for (int y = yPixelTopInt; y < yPixelBottomInt; y++) {
                double pixelRotationY = (y - yPixelTop) / (yPixelBottom - yPixelTop);
                int yTexture = (int) (8 * pixelRotationY);    
                pixels[x + y * width] = Texture.wall.pixels[(xTexture & 7) + (yTexture & 7) * 8];
                zBuffer[x + y * width] = 1 / (texture1 + (texture2 - texture1) * pixelRotation) * 2; 
            }
        }
    }
        
    /** limits the distance away for rendering */
    public void renderDistanceLimiter() {
        for (int i = 0; i < width * height; i++) {
            int color = pixels[i];
            int brightness = (int) (renderDistance / zBuffer[i]);
            
            /* minimum brightness value */
            if (brightness < 0) {
                brightness = 0;
            }
            
            /* maximum brightness value */
            if (brightness > 255) {
                brightness = 255;
            }
            
            int r = (color >> 16) & 0xff;
            int g = (color >> 8) & 0xff;
            int b = (color) & 0xff;
            
            r = r * brightness / 255;
            g = g * brightness / 255;
            b = b * brightness / 255;
            
            pixels[i] = r << 16 | g << 8 | b;
        }
    }
}