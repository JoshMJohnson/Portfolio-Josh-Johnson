package input;

/** handles user input controls */
public class Controller {
    public double x, y, z, rotation, xa, za, rotationa;
    public static boolean turnLeft = false;
    public static boolean turnRight = false;
    public static boolean walk = false;
    public static boolean crouchWalk = false;
    public static boolean runForward = false;
    
    /** game progression */
    public void tick(boolean forward, boolean backward, boolean left, 
                        boolean right, boolean jump, boolean crouch, boolean run) {
        /* action speed */
        double rotationSpeed = 0.01;
        double walkSpeed = 0.2;
        double xMovement = 0;
        double zMovement = 0;
        double jumpHeight = 0.5;
        double crouchHeight = 0.3;
                
        /* register forward movement */
        if (forward) {
            zMovement++;
            walk = true;
        }
        
        /* register backward movement */
        if (backward) {
            zMovement--;
            walk = true;
        }
        
        /* register left movement */
        if (left) {
            xMovement--;
            walk = true;
        }
        
        /* register right movement */
        if (right) {
            xMovement++;
            walk = true;
        }
        
        /* register turning left */
        if (turnLeft) {
            rotationa -= rotationSpeed;                      
        }
        
        /* register turning right */
        if (turnRight) {
            rotationa += rotationSpeed;                         
        }
        
        /* register jump */
        if (jump) {
            y += jumpHeight;
            run = false;
        }
        
        /* register a crouch */
        if (crouch) {
            y -= crouchHeight;
            walkSpeed = 0.05;
            run = false;
            crouchWalk = true;
        }
        
        /* register running */
        if (run) {
            walkSpeed = 0.5;
            walk = true;
            runForward = true;
        }
        
        /* control head bobbing when not moving */
        if (!forward && !backward && !left && !right) {
            walk = false;
        }
        
        /* control amount of head bobbing when moving and crouched */
        if (!crouch) {
            crouchWalk = false;
        }
        
        /* control amount of head bobbing when moving and sprinting */
        if (!run) {
            runForward = false;
        }
                
        /* handles changes in actions */
        xa += (xMovement * Math.cos(rotation) + zMovement * Math.sin(rotation)) * walkSpeed;
        za += (zMovement * Math.cos(rotation) - xMovement * Math.sin(rotation)) * walkSpeed;
        x += xa;
        y *= 0.9;
        z += za;
        xa *= 0.1;
        za *= 0.1;
        rotation += rotationa;
        rotationa *= 0.5;
    }
}