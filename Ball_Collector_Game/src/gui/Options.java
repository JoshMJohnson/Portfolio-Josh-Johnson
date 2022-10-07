package gui;

import java.awt.Choice;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;

import main.Display;

/** creates a window for the options menu */
public class Options extends Launcher {
    /* window settings */
    private int width = 800;
    private int height = 500;
   
    /* buttons */
    private JButton ok;
    private Rectangle rOK, rResolution;
    private Choice resolution = new Choice();
    
    /** constructor for Options class */
    public Options() {
        super(1);
        setTitle("Options -- Ball Collector Game");
        setSize(new Dimension(width, height));
        setLocationRelativeTo(null);
        drawButtons();
    }
    
    /** creates buttons within the option menu */
    private void drawButtons() {
        /* create buttons */
        ok = new JButton("ok");
        rOK = new Rectangle((width / 2) - (buttonWidth / 2), height - 100, buttonWidth, buttonHeight - 10);
        ok.setBounds(rOK);
        window.add(ok);
        
        /* change resolution option */
        rResolution = new Rectangle(50, 80,80, 25);
        resolution.setBounds(rResolution);
        resolution.add("640, 480");
        resolution.add("800, 600");
        resolution.add("1024, 768");
        resolution.select(0);
        window.add(resolution);
        
        /* action listeners */
        ok.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Display.selection = resolution.getSelectedIndex();
                dispose();
                new Launcher(0);
            }
        });
    }
}