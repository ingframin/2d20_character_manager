package mc3.main;
import java.awt.Dimension;
import java.util.HashMap;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import javax.swing.*;


public class MainFrame {
    JFrame wnd;
    HashMap<String,JButton> buttons;

    public MainFrame(){
        wnd = new JFrame();
        wnd.setTitle("Mutant Chronicles 3E - Character generator");
        wnd.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        wnd.setVisible(true);
        wnd.setSize(800, 720);
        wnd.setMinimumSize(new Dimension(800,720));
        buttons = new HashMap<>();
        buildUI();
        addCopyrightNote();
        wnd.pack();
    }    

    private void buildUI(){
        var content = wnd.getContentPane();
        var wheight = wnd.getHeight();
        var wwidth = wnd.getWidth();
        content.setBounds(10,10,wwidth-10,wheight-10);
        BorderLayout brdl = (BorderLayout)content.getLayout();
        brdl.setHgap(10);
        brdl.setHgap(10);
        //Load and show logo
        content.setBackground(new Color(0x373633));
        var logo = new ImageIcon("./visual/logo.png");
        var image = logo.getImage(); 
        int width = image.getWidth(null);
        int height = image.getHeight(null);
        var newimg = image.getScaledInstance(width/4, height/4,  java.awt.Image.SCALE_SMOOTH); // scale it the smooth way  
        var imageIcon = new ImageIcon(newimg);  // transform it back
        JLabel logoLbl = new JLabel(imageIcon);
        logoLbl.setMaximumSize(new Dimension(width/8,height/8));
        content.add(logoLbl,BorderLayout.NORTH);
        //Create buttons
        JButton standardMethodBtn = new JButton("Standard Method");
        standardMethodBtn.setSize(200, 40);
        standardMethodBtn.setMaximumSize(new Dimension(200,40));
        standardMethodBtn.setPreferredSize(new Dimension(200,40));
        standardMethodBtn.setMinimumSize(new Dimension(200,40));

        JButton twelveLPBtn = new JButton("12 Life Points");
        twelveLPBtn.setMaximumSize(new Dimension(200,40));
        twelveLPBtn.setSize(200, 40);
        twelveLPBtn.setPreferredSize(new Dimension(200,40));
        twelveLPBtn.setMinimumSize(new Dimension(200,40));

        JButton freeMethodBtn = new JButton("Free Method");
        freeMethodBtn.setSize(200, 40);
        freeMethodBtn.setMinimumSize(new Dimension(200,40));
        freeMethodBtn.setMaximumSize(new Dimension(200,40));
        freeMethodBtn.setPreferredSize(new Dimension(200,40));

        JPanel btnPane = new JPanel();
        var btnLayout = new GridLayout(1,3);

        btnPane.setLayout(btnLayout);

        buttons.put("standard", standardMethodBtn);
        buttons.put("12LP",twelveLPBtn);
        buttons.put("free",freeMethodBtn);
    
        btnPane.add(standardMethodBtn);
        btnPane.add(twelveLPBtn);
        btnPane.add(freeMethodBtn);

        btnPane.setBounds(0, 0, 600, 80);
        btnPane.setMaximumSize(new Dimension(600,80));
        btnPane.setMinimumSize(new Dimension(600,80));
        content.add(btnPane, BorderLayout.CENTER);

        
        
    }
    private void addCopyrightNote(){
        var content = wnd.getContentPane();
        //Add disclaimer label
        String disc = """
            <html>
           
                <style>
                    #link { color: #FF0000; } /* CSS link color */
                </style>
            <body>
            <p style=\"font-size:20pt;color: #FFAA33;font-weight: bold;\">
                Author: Franco Minucci (franco.minucci AT ingframin.eu)
            </p>
            <p style=\"font-size:16pt;color: #FFAA33;\">
            Character Generator tool for Mutant Chronicles 3rd edition RPG.
            The game is designed by Modiphius which holds the copyright on it and the 2d20 systems.
            <br/><br/>
            MUTANT CHRONICLES and related logos, characters, names, and distinctive likenesses thereof are trademarks or
            registered trademarks of Mutant Chronicles International Inc.<br/> 
            All rights reserved.<br/><br/>
            This software is provided as-is with GPLv3 license (<a style=\"color: #FFFF00; \" href=\"https://github.com/ingframin/mc3_character_generator\">Repository on Github</a>).
            <br/>
            This software is a fan made program: I have no relation with Modiphius nor the copyright holders of the Mutant Chronicles franchise.
            </p>
            </body>
            
            </html>
            """;
        
        JTextPane copyrightLabel = new JTextPane();
        copyrightLabel.setContentType("text/html");
        copyrightLabel.setText(disc);
        copyrightLabel.setEditable(false);
        copyrightLabel.setBackground(new Color(0x373633));
        content.add(copyrightLabel, BorderLayout.SOUTH);
    }
}
