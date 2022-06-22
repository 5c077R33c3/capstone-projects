package project.Poised;

import java.awt.Component;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.ComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Menu2Listener implements ActionListener {
	// Global variable declaration and initialization
	static JFrame mainWindow = new JFrame();
	static JPanel panel =  new JPanel();
	JButton next = new JButton("Next");
	static JButton save;
	
	static ArrayList<Integer> people_index= new ArrayList<Integer>();
	static ArrayList<String> people_temp = new ArrayList<String>();
	static ArrayList<Integer> project_index= new ArrayList<Integer>();
	static ArrayList<String> projects_temp = new ArrayList<String>();
	
	static JComboBox <String> choicePerson, choiceProject;
	static boolean proj = false;
	
	static JTextField name_TF, phone_TF, email_TF,address_TF;
	

	
	public void actionPerformed(ActionEvent click) {
	
		/* creation of string arrays for drop down menu, this is done by
		   iterating through the 'database' checking the class type of each
		   object stored within using the instanceof keyword. when true,
		   the object name is added to the arraylist of strings. 
		   the array list is then converted to an array.	
		 
		   the index of each project in the projects container is also saved
		   to be able to map the selected choice to the original container index
		 */
		for (int i = 0; i< Application.container.size(); i ++) {
			panel.removeAll();
			if(Application.container.get(i) instanceof Person) {
				people_temp.add(((Person) Application.container.get(i)).getName() + "(" + ((Person) Application.container.get(i)).getTitle() + ")");
				people_index.add(i);
			}
			else if(Application.container.get(i) instanceof Project) {
				projects_temp.add(((Project) Application.container.get(i)).getProjectName() + "(" + ((Project) Application.container.get(i)).getBuilding() + ")");
				project_index.add(i);
			}
		}
		// Conversion of Arraylists to array list
		String people[] = people_temp.toArray(new String[people_temp.size()]);
		String projects[] = projects_temp.toArray(new String[projects_temp.size()]);
		
		// frame and panel containing main menu window elements	
		mainWindow.setTitle("Update Existing");
		mainWindow.setSize(337, 300);
		mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// Panel orientation and layout
		panel.setLayout(null);
		mainWindow.add(panel);
		
		// Update existing information second menu
		// Person Chosen from first level menu
		if(click.getSource() == Application.person) {
			// Initialization of GUI components
			choicePerson = new JComboBox<String>(people);
			choicePerson.setBounds(10, 10, 300, 25);
			panel.add(choicePerson);
			
		
		}
		// Project chosen from first level  menu
		else if (click.getSource() == Application.project) {
			proj = true;
			
			// Initialization of GUI components
			choiceProject = new JComboBox<String>(projects);
			choiceProject.setBounds(10, 10, 300, 25);
			panel.add(choiceProject);			
			
		}
		
		// Initialization of GUI buttons
		next.setBounds(10, 80, 80, 25);
		panel.add(next);
		next.addActionListener(new nextListener());
		mainWindow.setVisible(true);

	}

	
	public class nextListener implements ActionListener {

		@Override
		
		public void actionPerformed(ActionEvent click) {
			// Initialization of GUI components
			panel.removeAll();
			mainWindow.setSize(500, 300);
			mainWindow.add(panel);
			mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			save = new JButton("Save");
			save.addActionListener(new SaveListener());
			save.setBounds(10, 165, 80, 25);
			panel.add(save);
			
			// Project button selected in first level menu
			if (proj == true){
				// Initialization of GUI components
				// Paid to date (PtD)
				JLabel label_PtD = new JLabel("Paid to Date");
				label_PtD.setBounds(10, 10, 150, 25);
				Application.PtD_TF = new JTextField(30);
				Application.PtD_TF.setBounds(150, 10, 300, 25);
				panel.add(label_PtD);
				panel.add(Application.PtD_TF);
				
				// Deadline
				JLabel label_deadline = new JLabel("Deadline");
				label_deadline.setBounds(10, 40, 150, 25);
				Application.deadline_TF = new JTextField(30);
				Application.deadline_TF.setBounds(150, 40, 300, 25);
				panel.add(label_deadline);
				panel.add(Application.deadline_TF);				
				
			}else {
				// Initialization of GUI components
				// PERSON DETAILS
				JLabel details = new JLabel("Person Details");
				details.setAlignmentX(FlowLayout.CENTER);
				details.setBounds(200, 10, 150, 25);
				
				// Name and surname
				JLabel person_label = new JLabel("Name and Surname");
				person_label.setBounds(10, 40, 150, 25);
				name_TF = new JTextField(30);
				name_TF.setBounds(150, 40, 300, 25);
				panel.add(person_label);
				panel.add(name_TF);
				panel.add(details);
				
				// Phone				
				JLabel phone_label = new JLabel("Phone number");
				phone_label.setBounds(10, 70, 150, 25);
				phone_TF = new JTextField(30);
				phone_TF.setBounds(150, 70, 300, 25);
				panel.add(phone_label);
				panel.add(phone_TF);
				
				// Email
				JLabel email_label = new JLabel("email");
				email_label.setBounds(10, 100, 150, 25);
				email_TF = new JTextField(30);
				email_TF.setBounds(150, 100, 300, 25);
				panel.add(email_label);
				panel.add(email_TF);
				
				// Address
				JLabel address_label = new JLabel("Physical Address");
				address_label.setBounds(10, 130, 150, 25);
				address_TF = new JTextField(30);
				address_TF.setBounds(150, 130, 300, 25);
				panel.add(address_label);
				panel.add(address_TF);
			}
			
			
			mainWindow.setVisible(true);
			

		}

	}

}
