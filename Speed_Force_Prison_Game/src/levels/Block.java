package levels;

import graphics.Sprite;
import java.util.ArrayList;
import java.util.List;

public class Block {
    public boolean solid = false;
    public static Block solidWall = new SolidBlock();
    public List<Sprite> sprites = new ArrayList<Sprite>();
    
    /** adds a sprite to the list of sprites */
    public void addSprite(Sprite sprite) {
        sprites.add(sprite);
    }
}