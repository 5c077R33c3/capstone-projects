package project.Poised;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import project.Poised.SaveListener;

class MenuListener implements ActionListener{
	
	// Declaration of globally accessible variable instances
	static JButton save;
	static JComboBox <String> choiceProject;
	static ArrayList<Integer> project_index= new ArrayList<Integer>();
	static ArrayList<String> projects_temp = new ArrayList<String>();
	static JTextField completionDate_TF, totalFee_TF;
	static String tag;


	public void actionPerformed(ActionEvent click) {
		
		// Initialization of GUI components
		JFrame mainWindow = new JFrame();
		JPanel panel =  new JPanel();
		
		mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		
		panel.setLayout(null);
		mainWindow.add(panel);
		
		save = new JButton("Save");
		int index ;
		
		
		// flow control controlling the action to execute for each button is clicked
		// New Project			
		if (click.getSource() == Application.newProject) {
			tag = "NewProject";
			
			// Declaration and initialization of GUI components
			panel.removeAll();
			mainWindow.setSize(500, 830);
			
			JLabel client_details, client, client_phone, client_email, client_address,
			architect_details, architect, archi_phone, archi_email, archi_address,
			contractor_details, contractor, contra_phone, contra_email, contra_address;
					
			mainWindow.setTitle("Project Details");
			
			// Client Details
			client_details = new JLabel("Client Details");
			client_details.setAlignmentX(FlowLayout.CENTER);
			client_details.setBounds(200, 5, 100, 25);
			
			// Name and Surname
			client = new JLabel("Name and Surname");
			client.setBounds(10, 35, 150, 25);
			Application.client_TF = new JTextField(30);
			Application.client_TF.setBounds(150, 35, 300, 25);
			panel.add(client);
			panel.add(Application.client_TF);
			panel.add(client_details);
			
			// Phone				
			client_phone = new JLabel("Phone number");
			client_phone.setBounds(10, 65, 150, 25);
			Application.client_phoneTF = new JTextField(30);
			Application.client_phoneTF.setBounds(150, 65, 300, 25);
			panel.add(client_phone);
			panel.add(Application.client_phoneTF);
			// Email
			client_email = new JLabel("email");
			client_email.setBounds(10, 95, 150, 25);
			Application.client_emailTF = new JTextField(30);
			Application.client_emailTF.setBounds(150, 95, 300, 25);
			panel.add(client_email);
			panel.add(Application.client_emailTF);
			// Address
			client_address = new JLabel("Physical Address");
			client_address.setBounds(10, 125, 150, 25);
			Application.client_addressTF = new JTextField(30);
			Application.client_addressTF.setBounds(150, 125, 300, 25);
			panel.add(client_address);
			panel.add(Application.client_addressTF);
			
			// ARCHITECT DETAILS
			architect_details = new JLabel("Architect Details");
			architect_details.setAlignmentX(FlowLayout.CENTER);
			architect_details.setBounds(193, 160, 150, 25);
			// Name and surname
			architect = new JLabel("Name and Surname");
			architect.setBounds(10, 190, 150, 25);
			Application.archi_TF = new JTextField(30);
			Application.archi_TF.setBounds(150, 190, 300, 25);
			panel.add(architect);
			panel.add(Application.archi_TF);
			panel.add(architect_details);
			// Phone
			archi_phone = new JLabel("Phone number");
			archi_phone.setBounds(10, 220, 150, 25);
			Application.archi_phoneTF = new JTextField(30);
			Application.archi_phoneTF.setBounds(150, 220, 300, 25);
			panel.add(archi_phone);
			panel.add(Application.archi_phoneTF);
			// Email
			archi_email = new JLabel("email");
			archi_email.setBounds(10, 250, 150, 25);
			Application.archi_emailTF = new JTextField(30);
			Application.archi_emailTF.setBounds(150, 250, 300, 25);
			panel.add(archi_email);
			panel.add(Application.archi_emailTF);
			// Address
			archi_address = new JLabel("Physical Address");
			archi_address.setBounds(10, 280, 150, 25);
			Application.archi_addressTF = new JTextField(30);
			Application.archi_addressTF.setBounds(150, 280, 300, 25);
			panel.add(archi_address);
			panel.add(Application.archi_addressTF);
			
			// CONTRACTOR DETAILS
			contractor_details = new JLabel("Contractor Details");
			contractor_details.setAlignmentX(FlowLayout.CENTER);
			contractor_details.setBounds(190, 315, 150, 25);
			
			// Name and surname
			contractor = new JLabel("Name and Surname");
			contractor.setBounds(10, 345, 150, 25);
			Application.contractor_TF = new JTextField(30);
			Application.contractor_TF.setBounds(150, 345, 300, 25);
			panel.add(contractor);
			panel.add(Application.contractor_TF);
			panel.add(contractor_details);
			
			// Phone				
			contra_phone = new JLabel("Phone number");
			contra_phone.setBounds(10, 375, 150, 25);
			Application.contra_phoneTF = new JTextField(30);
			Application.contra_phoneTF.setBounds(150, 375, 300, 25);
			panel.add(contra_phone);
			panel.add(Application.contra_phoneTF);
			
			// Email
			contra_email = new JLabel("email");
			contra_email.setBounds(10, 405, 150, 25);
			Application.contra_emailTF = new JTextField(30);
			Application.contra_emailTF.setBounds(150, 405, 300, 25);
			panel.add(contra_email);
			panel.add(Application.contra_emailTF);
			
			// Address
			contra_address = new JLabel("Physical Address");
			contra_address.setBounds(10, 435, 150, 25);
			Application.contra_addressTF = new JTextField(30);
			Application.contra_addressTF.setBounds(150, 435, 300, 25);
			panel.add(contra_address);
			panel.add(Application.contra_addressTF);			
			
			// PROJECT DETAILS
			JLabel project_details = new JLabel("Project Details");
			project_details.setAlignmentX(FlowLayout.CENTER);
			project_details.setBounds(200, 470, 150, 25);
			
			// Project Number
			JLabel label_projectNumber = new JLabel("Project Number");
			label_projectNumber.setBounds(10, 500, 150, 25);
			Application.projectNUmber_TF = new JTextField(30);
			Application.projectNUmber_TF.setBounds(150, 500, 300, 25);
			panel.add(label_projectNumber);
			panel.add(Application.projectNUmber_TF);
			panel.add(project_details);
			
			// Project Name
			JLabel label_projectName = new JLabel("Project Name");
			label_projectName.setBounds(10, 530, 150, 25);
			Application.projectName_TF = new JTextField(30);
			Application.projectName_TF.setBounds(150, 530, 300, 25);
			panel.add(label_projectName);
			panel.add(Application.projectName_TF);
			
			// Building
			JLabel label_building = new JLabel("Building Type");
			label_building.setBounds(10, 560, 150, 25);
			Application.building_TF = new JTextField(30);
			Application.building_TF.setBounds(150, 560, 300, 25);
			panel.add(label_building);
			panel.add(Application.building_TF);
			
			// Address
			JLabel label_buildingAddress = new JLabel("Physical Address");
			label_buildingAddress.setBounds(10, 590, 150, 25);
			Application.buildingAddress_TF = new JTextField(30);
			Application.buildingAddress_TF.setBounds(150, 590, 300, 25);
			panel.add(label_buildingAddress);
			panel.add(Application.buildingAddress_TF);
			
			// erf
			JLabel label_ERF = new JLabel("ERF");
			label_ERF .setBounds(10, 620, 150, 25);
			Application.ERF_TF = new JTextField(30);
			Application.ERF_TF.setBounds(150, 620, 300, 25);
			panel.add(label_ERF );
			panel.add(Application.ERF_TF);
			
			// Total Fee				
			JLabel label_fee = new JLabel("Total Fee");
			label_fee.setBounds(10, 650, 150, 25);
			Application.fee_TF = new JTextField(30);
			Application.fee_TF.setBounds(150, 650, 300, 25);
			panel.add(label_fee);
			panel.add(Application.fee_TF);			
			
			// Save Button
			save.setBounds(10, 740, 80, 25);
			panel.add(save);
			save.addActionListener(new SaveListener());
			
		}
		// Update Existing
		else if(click.getSource() == Application.updateExisting) {
			tag = "UpdateExisting";
			
			mainWindow.setTitle("Update Existing");
							
			// frame and panel containing main menu window elements		
			mainWindow.setSize(300, 300);
			mainWindow.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			
			// Panel orientation and layout
			panel.setLayout(new FlowLayout(FlowLayout.CENTER));
			mainWindow.add(panel);
			
			// ADDING BUTTONS
			// Project button
			Application.project = new JButton("Project");
			Application.project.addActionListener(new Menu2Listener());
			panel.add(Application.project);		
			
			// Person button
			Application.person = new JButton("Person");
			Application.person.addActionListener(new Menu2Listener());
			panel.add(Application.person);
		}
		// Finalize Project
		else if(click.getSource() == Application.finalizeProj) {
			panel.removeAll();
			tag = "FinalizeProject";
			
			// Initialization and declaration of GUI components
			mainWindow.setSize(500, 300);			
			
			// Completion date label and text field
			JLabel CompletionDate_label = new JLabel("Completion Date");
			completionDate_TF = new JTextField();
			CompletionDate_label.setBounds(10, 40, 150, 25);
			completionDate_TF.setBounds(150, 40, 300, 25);
			panel.add(completionDate_TF);
			panel.add(CompletionDate_label);
			
			// Total fee label and text field
			JLabel Fee_label = new JLabel("Total Fee");
			totalFee_TF = new JTextField();
			Fee_label.setBounds(10, 70, 150, 25);
			totalFee_TF.setBounds(150, 70, 300, 25);
			panel.add(Fee_label);
			panel.add(totalFee_TF);
			
			/* creation of string arrays for drop down menu, this is done by
			   iterating through the 'database' checking the class type of each
			   object stored within using the instance of keyword. when true,
			   the project name is added to the arraylist of strings. 
			   the array list is then converted to an array.	
			 
			   the index of each project in the projects container is also saved
			   to be able to map the selected choice to the original container index
			 */
			for (int i = 0; i< Application.container.size(); i ++) {
				 if(Application.container.get(i) instanceof Project) {
					projects_temp.add(((Project) Application.container.get(i)).getProjectName() + "(" + ((Project) Application.container.get(i)).getBuilding() + ")");
					project_index.add(i);
				}
			}
			// conversion of arraylist to array
			String projects[] = projects_temp.toArray(new String[projects_temp.size()]);
			
			// initialization of GUI components
			choiceProject = new JComboBox<String>(projects);
			choiceProject.setBounds(10, 10, 300, 25);
			panel.add(choiceProject);
			
			save.setBounds(10, 105, 80, 25);
			panel.add(save);
			save.addActionListener(new SaveListener());
			
			/* 'mapping' the item selected from the generated array of strings used in 
			 * the drop down menu to the items in the container using the index stored
			 *  in the list of indices
			 */
			for(int i = 0; i < projects_temp.size(); i ++) {
				if (choiceProject.getItemAt(choiceProject.getSelectedIndex()) == projects_temp.get(i)) {
					 index = project_index.get(i);
				}
			}
		}
		// View incomplete Project
		else if(click.getSource() == Application.vuIncomplete) {
			panel.removeAll();
			System.out.println("VI clicked");
			mainWindow.setTitle("Client Info");
		}
		// View Overdue Projects
		else if(click.getSource() == Application.vuOverdue) {
			panel.removeAll();
			System.out.println("VO clicked");
			mainWindow.setTitle("Client Info");
		}
		// Search
		else if(click.getSource() == Application.search) {
			panel.removeAll();
			System.out.println("S clicked");
			mainWindow.setTitle("Client Info");
		}
				
		mainWindow.setVisible(true);
	}
	
	
	
}