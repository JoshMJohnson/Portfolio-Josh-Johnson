package gui;

import java.awt.Choice;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JLabel;

import main.Display;

/** creates a window for the options menu */
public class Options extends Launcher {
    /* window settings */
    private int windowWidth = 300;
    private int windowHeight = 400;
   
    /* buttons */
    private JButton ok;
    private Rectangle rOK, rResolution;
    private Choice resolution = new Choice();
    private JLabel resLabel = new JLabel();
      
    /** constructor for Options class */
    public Options() {
        super(1);
        setTitle("Options -- Ball Collector Game");
        setSize(new Dimension(windowWidth, windowHeight));
        setLocationRelativeTo(null);
        drawButtons();
    }
    
    /** creates buttons within the option menu */
    private void drawButtons() {
        /* create buttons */
        ok = new JButton("Save");
        rOK = new Rectangle((windowWidth / 2) - (buttonWidth / 2), windowHeight - 100, buttonWidth, buttonHeight - 10);
        ok.setBounds(rOK);
        window.add(ok);
        
        /* change resolution option */
        /* label */
        int resLabelWidth = 90;
        int resLabelHeight = 20;
        
        resLabel = new JLabel("Change Resolution");
        resLabel.setBounds((windowWidth / 2) - (resLabelWidth / 2), 10, resLabelWidth, resLabelHeight);
        window.add(resLabel);
                
        /* drop-down box */
        rResolution = new Rectangle((windowWidth / 2) - (resLabelWidth / 2) , 20 + resLabelHeight, 90, 30);
        resolution.setBounds(rResolution);
        resolution.add("640 x 480");
        resolution.add("800 x 600");
        resolution.add("1024 x 768");
        resolution.add("1400 x 1000");
        resolution.select(0);
        window.add(resolution);
        
        /* action listeners */
        /* submit button */
        ok.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Display.selection = resolution.getSelectedIndex();
                dispose();
                new Launcher(0);
            }
        });
    }
}