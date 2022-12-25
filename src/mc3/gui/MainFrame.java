package mc3.gui;
import java.awt.Dimension;
import java.util.HashMap;
import javax.swing.*;


public class MainFrame {
    JFrame wnd;
    HashMap<String,JButton> buttons;

    public MainFrame(){
        wnd = new JFrame();
        wnd.setTitle("Mutant Chronicles 3E - Character generator");
        wnd.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        wnd.setVisible(true);
        wnd.setSize(800, 620);
        wnd.setMaximumSize(new Dimension(800, 620));
        wnd.setPreferredSize(new Dimension(800, 620));
        wnd.setResizable(false);
        buttons = new HashMap<>();
        
        StartScreen sc = new StartScreen();
        sc.buttons.get("standard").addActionListener((e)->{
            if(e.getActionCommand().equals("Standard Method")){
                wnd.setContentPane(new StartingAttributes());
                wnd.pack();
            }
        });    
        wnd.setContentPane(sc);
        
        wnd.pack();
    }   


   
}
