package input;

/** handles user input controls */
public class Controller {
    public double x, z, rotation, xa, za, rotationa;
    
    /** game progression */
    public void tick(boolean forward, boolean backward, boolean left, boolean right, boolean turnLeft, boolean turnRight) {
        /* action speed */
        double rotationSpeed = 0.01;
        double walkSpeed = 0.2;
        double xMovement = 0;
        double zMovement = 0;
        
        /* register forward movement */
        if (forward) {
            zMovement++;
        }
        
        /* register backward movement */
        if (backward) {
            zMovement--;
        }
        
        /* register left movement */
        if (left) {
            xMovement--;
        }
        
        /* register right movement */
        if (right) {
            xMovement++;
        }
        
        /* register turning left */
        if (turnLeft) {
            rotationa -= rotationSpeed;
        }
        
        /* register turning right */
        if (turnRight) {
            rotationa += rotationSpeed;
        }
        
        xa += (xMovement * Math.cos(rotation) + zMovement * Math.sin(rotation)) * walkSpeed;
        za += (zMovement * Math.cos(rotation) - xMovement * Math.sin(rotation)) * walkSpeed;

        
        x += xa;
        z += za;
        xa *= 0.1;
        za *= 0.1;
        rotation += rotationa;
        rotationa *= 0.5;
    }
}