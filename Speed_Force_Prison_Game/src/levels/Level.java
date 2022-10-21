package levels;

import graphics.Render3D;
import graphics.Sprite;

import java.util.Random;

import main.Display;

/** creates a layout for the level */
public class Level {
    public Block[] arenaBlocks; 
    public final int arenaWidth, arenaHeight;
    
    /** constructor for the Level class */
    public Level(int width, int height) {
        this.arenaWidth = width;
        this.arenaHeight = height;
        arenaBlocks = new Block[width * height];
                
        /* gets number of blurs needed to be collected before games is won */
        int numBlurs = Display.blurs;
        
        if (Display.difficulty == 2) { /* if second hardest difficulty */
            numBlurs = (int) (Math.floor(numBlurs * 1.5));
        } else if (Display.difficulty == 3) { /* if hardest difficulty */
            numBlurs = (int) (Math.floor(numBlurs * 2));
        }
        
        int blurChance = (int) Math.ceil(Render3D.arenaBorderSize * 2 / numBlurs); /* adjusts amount of blurs to win game based on difficulty */        
        Random random = new Random();  
        
        System.out.println("numBlurs: " + numBlurs);
        System.out.println("blurChance: " + blurChance);
        System.out.println("arenaBroderSize: " + Render3D.arenaBorderSize);

        /* render blocks */
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                Block block = null;
                
                if (random.nextInt(6) == 0) { /* likelihood of rendering a wall */
                    block = new SolidBlock();
                } else {
                    block = new Block();
                    
                    if (random.nextInt(blurChance) == 0) { /* places sprite on one out of every 5 open tiles */
                        block.addSprite(new Sprite(0, 0, 0));
                    }
                }
                
                arenaBlocks[x + y * width] = block;
            }
        }
    }
    
    /** creates a block */
    public Block create(int x, int y) {
        if (x < 0 || y < 0 || x >= arenaWidth || y >= arenaHeight) {
            return Block.solidWall;
        }
        
        return arenaBlocks[x + y * arenaWidth];
    }
}