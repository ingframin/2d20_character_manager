package mc3.main;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextPane;
import javax.swing.plaf.InsetsUIResource;
import javax.swing.text.SimpleAttributeSet;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.awt.Font;
import java.util.HashMap;
import java.awt.Color;
import java.awt.Dimension;

public class StartScreen extends JPanel{

    HashMap<String,JButton> buttons;

    public StartScreen(){
        super();
        buttons = new HashMap<>();
        buildUI();
        addCopyrightNote();
    }

    private void buildUI(){
        var wheight = getHeight();
        var wwidth = getWidth();
        this.setBounds(10,20,wwidth-10,wheight+10);
        BorderLayout brdl = new BorderLayout();
        this.setLayout(brdl);
        brdl.setHgap(10);
        brdl.setHgap(10);
        //Load and show logo
        this.setBackground(new Color(0x373633));
        var logo = new ImageIcon("./visual/logo.png");
        var image = logo.getImage(); 
        int width = image.getWidth(null);
        int height = image.getHeight(null);
        var newimg = image.getScaledInstance(width/4, height/4,  java.awt.Image.SCALE_SMOOTH); // scale it the smooth way  
        var imageIcon = new ImageIcon(newimg);  // transform it back
        JLabel logoLbl = new JLabel(imageIcon);
        logoLbl.setMaximumSize(new Dimension(width/4,height/4));
        this.add(logoLbl,BorderLayout.NORTH);
        //Create buttons
        

        JButton standardMethodBtn = new JButton("Standard Method");
        styleButton(standardMethodBtn);

        JButton twelveLPBtn = new JButton("12 Life Points");
        styleButton(twelveLPBtn);

        JButton freeMethodBtn = new JButton("Free Method");
        styleButton(freeMethodBtn);

        JPanel btnPane = new JPanel();
        btnPane.setMaximumSize(new Dimension(600,80));
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
        btnPane.setPreferredSize(new Dimension(600,80));
        btnPane.setSize(new Dimension(600,80));
       
        this.add(btnPane, BorderLayout.CENTER);

        
        
    }

    private void styleButton(JButton btn){
        btn.setSize(200, 40);
        btn.setMaximumSize(new Dimension(200,40));
        btn.setPreferredSize(new Dimension(200,40));
        btn.setMinimumSize(new Dimension(200,40));
        Font btnFont = new Font(btn.getFont().getName(),btn.getFont().getStyle(),20);
        btn.setFont(btnFont);
        btn.setBackground(Color.DARK_GRAY);
        btn.setForeground(Color.WHITE);
        btn.setBorderPainted(true);


    }
    private void addCopyrightNote(){
        
        //Add disclaimer label
        String disc = "";
        try {
            disc = new String(Files.readAllBytes(Paths.get("visual/copyright.html")));
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        var copyrightLabel = new JTextPane();
        copyrightLabel.setContentType("text/html");
        copyrightLabel.setText(disc);
        
        copyrightLabel.setBackground(Color.DARK_GRAY);
        copyrightLabel.setForeground(Color.WHITE);
        copyrightLabel.setMargin(new InsetsUIResource(20, 10, 20, 10));
        copyrightLabel.setFont(new Font("Dialog", Font.PLAIN, 14));
        SimpleAttributeSet atset = new SimpleAttributeSet();
        atset.addAttribute(copyrightLabel, atset);       

        copyrightLabel.setEditable(false);
        this.add(copyrightLabel, BorderLayout.SOUTH);
    }
    
}
