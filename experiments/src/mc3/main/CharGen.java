package mc3.main;

import javax.swing.SwingUtilities;

import mc3.gui.MainFrame;


public class CharGen{

    public static void main(String[] args) {
                        
        SwingUtilities.invokeLater(()->{new MainFrame();});

    }
}