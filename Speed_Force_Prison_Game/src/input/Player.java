package input;

/** handles user input controls */
public class Player {
    /* player movement */
    public static double x, y, z, rotation;
    public static boolean turnLeft = false;
    public static boolean turnRight = false;
    public static boolean walk = false;
    public static boolean crouchWalk = false;
    public static boolean runForward = false;
    public double xa, za, rotationa;

    /* collisions variables */
    public static boolean forwardCollision = false;
    public static boolean backwardCollision = false;
    public static boolean leftCollision = false;
    public static boolean rightCollision = false;
    
    /* indicated direction of player */
    public static boolean forwardDirection = false;
    public static boolean backwardDirection = false;
    public static boolean leftDirection = false;
    public static boolean rightDirection = false;
    
    /** constructor for the Player class */
    public Player(double x, double z, double rotation) {
        Player.x = x;
        Player.z = z;
        Player.rotation = rotation;
    }
    
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
        
        /* direction indications */
        forwardDirection = forward;
        backwardDirection = backward;
        leftDirection = left;
        rightDirection = right;
        
        /* register forward movement */
        if (forward) {
            if (!forwardCollision) {
                zMovement++;
                walk = true;
            }
        }
        
        /* register backward movement */
        if (backward) {
            if (!backwardCollision) {
                zMovement--;
                walk = true;
            }
        }

        /* register left movement */
        if (left) {
            if (!leftCollision) {
                xMovement--;
                walk = true;
            }
        }
        
        /* register right movement */
        if (right) {
            if (!rightCollision) {
                xMovement++;
                walk = true;
            }
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
        
        /* resetting collisions */
        forwardCollision = false;
        leftCollision = false;
        rightCollision = false;
        backwardCollision = false;
    }
}