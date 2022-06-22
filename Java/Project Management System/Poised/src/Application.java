package project.Poised;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Application {
	// Initialization of variable instances accessible to all classes in the package
	static boolean returnTo = false;
	static JButton newProject;
	static JButton updateExisting;
	static JButton finalizeProj;
	static JButton vuIncomplete;
	static JButton vuOverdue;
	static JButton search;
	static JButton save;
	static JButton project;
	static JButton person;
	static Container container = new Container() ;
	static JTextField client_TF, client_phoneTF, client_emailTF, client_addressTF,
	archi_TF, archi_phoneTF, archi_emailTF, archi_addressTF, contractor_TF,
	contra_phoneTF, contra_emailTF, contra_addressTF, projectNUmber_TF,
	projectName_TF, building_TF, buildingAddress_TF, ERF_TF, fee_TF, PtD_TF, deadline_TF;


	public static void main(String[] args) {
		// if conditional run during the start of the application to initialize test objects
		// Upon returning to the main menu the returnTo variable is changed to true
		if (returnTo == false) {
			
		// variable declaration and initialization	
		Person client1, architect1, contractor1;
		Project project1;
		
		client1 = new Person("James", "0732745263", "james@Boanerges.com", "77 Heaven lane", "Client");
		architect1 = new Person("GodKnows", "777", "father@Heaven.com", "Heaven", "Architect");
		contractor1 = new Person("The Holy Spirit", "777", "HS@heaven.com", "Heaven", "Contractor");
		
		project1 = new Project("02711", "Mansion within", "Mansion", "77 Heaven Lane", "7755", architect1,
				contractor1, client1);
		
		// storing of test objects
		container.add(project1);
		container.add(architect1);
		container.add(client1);
		container.add(contractor1);	
		}
		
		// Initialization of GUI components
		JFrame mainWindow = new JFrame();
		JPanel panel =  new JPanel();
		
		// frame and panel containing main menu window elements
		mainWindow.setTitle("Main Menu");		
		mainWindow.setSize(300, 300);
		mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// Panel orientation and layout
		panel.setLayout(new FlowLayout(FlowLayout.CENTER));
		mainWindow.add(panel);
		
		// ADDING BUTTONS
		// New Project button
		newProject = new JButton("New Project");
		newProject.addActionListener(new MenuListener());
		panel.add(newProject);		
		
		// Update Existing button
		updateExisting = new JButton("Update Existing Project");
		updateExisting.addActionListener(new MenuListener());
		panel.add(updateExisting);
		
		// Finalize project button
		finalizeProj = new JButton("Finalize Project");
		finalizeProj.addActionListener(new MenuListener());
		panel.add(finalizeProj);
		
		// View incomplete projects button
		vuIncomplete = new JButton("View Incomplete Projects");
		vuIncomplete.addActionListener(new MenuListener());
		panel.add(vuIncomplete);
		
		// View Overdue projects button
		vuOverdue = new JButton("View Overdue Projects");
		vuOverdue.addActionListener(new MenuListener());
		panel.add(vuOverdue);
		
		// Search button
		search = new JButton("Search");
		search.addActionListener(new MenuListener());
		panel.add(search);	
		
		
		mainWindow.setVisible(true);
	}

}
