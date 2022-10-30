package levels;

import graphics.Blur;
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
                
        generateLevel();
    }
    
    /** sets up the level */
    private void generateLevel() {
        int numBlurs = Display.blurs; /* gets number of blurs needed to be collected before games is won */
        
        if (Display.difficulty == 2) { /* if second hardest difficulty */
            numBlurs = (int) (Math.floor(numBlurs * 1.5));
        } else if (Display.difficulty == 3) { /* if hardest difficulty */
            numBlurs = (int) (Math.floor(numBlurs * 2));
        }
        
        int blurChance = (int) Math.ceil(3000 / numBlurs); /* adjusts amount of blurs to win game based on difficulty */        
        int wallChance = 6;        
        Random random = new Random(); 
        
        System.out.println("arenaHeight: " + arenaHeight);
        System.out.println("arenaWidth: " + arenaWidth);
        
        /* render blocks */
        for (int y = 0; y < arenaHeight; y++) {
            for (int x = 0; x < arenaWidth; x++) {
                Block block = null;
                
                if ((random.nextInt(wallChance) == 0) 
                        && (x > 5) && (y > 5) && (x < arenaWidth - 5) && (y < arenaHeight - 5)) { /* likelihood of rendering a wall excluding running lanes */
                    block = new SolidBlock();
                } else {
                    block = new Block();
                    
                    if (random.nextInt(blurChance) == 0) { /* places a blur on one out of every 'blurChance;value' tiles */
                        block.addBlur(new Blur(0.5, 0, 0.5));
                    }
                }
                
                arenaBlocks[x + y * arenaWidth] = block;
            }
        }
    }
    
    /** creates a block */
    public Block create(int x, int y) {
        if (x < 0 || y < 0 || x >= arenaWidth || y >= arenaHeight) { /* wall border around arena */
            return Block.solidWall;
        }
        
        return arenaBlocks[x + y * arenaWidth]; /* arena grid */
    }
}