package project.Poised;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SaveListener implements ActionListener{
	/*
	 *  save listener runs whenever the save button is clicked . the class method 
	 *  saves all intended data and then returns to the main menu.
	 * */

	
	public void actionPerformed(ActionEvent click) {
		// closing the test object initiation in Application class
		Application.returnTo = true;
		
		// index initialization
		Integer index = null;
		
		// when the save button is clicked in new project
		if(click.getSource() == MenuListener.save && MenuListener.tag == "NewProject") {
			
			// initialization of string data for project and person object initialization
			// this is done by fetching the string information entered in the textfields 
			// stored in the Application class
			String client = Application.client_TF.getText();
			String client_phone = Application.client_phoneTF.getText();
			String client_email = Application.client_emailTF.getText();
			String client_address = Application.client_addressTF.getText() ;
			String architect = Application.archi_TF.getSelectedText();
			String archi_phone = Application.archi_phoneTF.getText();
			String archi_email = Application.archi_emailTF.getText();
			String archi_address = Application.archi_addressTF.getText();
			String contractor = Application.contractor_TF.getText();
			String contra_phone = Application.contra_phoneTF.getText();
			String contra_Email = Application.contra_emailTF.getText();
			String contra_address = Application.contra_addressTF.getText();
			String projectNumber = Application.projectNUmber_TF.getText();
			String projectName = Application.projectName_TF.getText();
			String buiding = Application.building_TF.getText();
			String erf = Application.ERF_TF.getText();
			String buildingAddress = Application.buildingAddress_TF.getText();
			String fee = Application.fee_TF.getText();
			String PtD = Application.PtD_TF.getText();
			String deadline = Application.deadline_TF.getText();
			
			// Person and Project object initialization.
			Person clientPerson = new Person(client, client_phone, client_email, client_address, "Client");
			Person ArchiPerson = new Person(architect, archi_phone, archi_email, archi_address, "Architect");
			Person ContraPerson = new Person(contractor, contra_phone, contra_Email, contra_address, "Contractor");
			Project NewProject = new Project(projectNumber, projectName, buiding, buildingAddress, erf, ArchiPerson, ContraPerson, clientPerson);
			
			// Adding objects to container class
			Application.container.add(clientPerson);
			Application.container.add(ArchiPerson);
			Application.container.add(ContraPerson);
			Application.container.add(NewProject);
			
			
		}// Save button clicked in Menu2Listener for update existing
		else if (click.getSource() == Menu2Listener.save && MenuListener.tag == "UpdateExisting" ) {
			// Update existing project
			if (Menu2Listener.proj == true) {
				/*
				 * Mapping the selected string index to the object index in the container,
				 * this is done by accessing the index information stored in Menu2Listener
				 * then assigning it to the index variable
				 * */
				for(int i = 0; i < Menu2Listener.projects_temp.size(); i ++) {
					if (Menu2Listener.choiceProject.getItemAt(Menu2Listener.choiceProject.getSelectedIndex()) == Menu2Listener.projects_temp.get(i)) {
						 index = Menu2Listener.project_index.get(i);
					}
				}
				// updating selected item with new information
				String deadline = Application.deadline_TF.getText();
				((Project) Application.container.get(index)).setDeadline(deadline);
				
				String PtD = Application.PtD_TF.getText();
				((Project) Application.container.get(index)).setPaidToDate(PtD);
				
			}
			// update existing person
			else {
				/*
				 * Mapping the selected string index to the object index in the container,
				 * this is done by accessing the index information stored in Menu2Listener
				 * then assigning it to the index variable
				 * */
				for(int i = 0; i < Menu2Listener.people_temp.size(); i ++) {
					if (Menu2Listener.choicePerson.getItemAt(Menu2Listener.choicePerson.getSelectedIndex()) == Menu2Listener.people_temp.get(i)) {
						index = i;
					}
				}
				 
				// updating selected item with new information
				String name = Menu2Listener.name_TF.getText();
				((Person) Application.container.get(index)).setName(name);
				
				String phone = Menu2Listener.phone_TF.getText();
				((Person) Application.container.get(index)).setPhone(phone);
				
				String email = Menu2Listener.email_TF.getText();
				((Person) Application.container.get(index)).setEmail(email);
				
				String address = Menu2Listener.address_TF.getText();
				((Person) Application.container.get(index)).setAddress(address);
								
				
			}
			
		}
		else if (click.getSource() == MenuListener.save && MenuListener.tag == "FinalizeProject") {
			
			/*
			 * Mapping the selected string index to the object index in the container,
			 * this is done by accessing the index information stored in Menu2Listener
			 * then assigning it to the index variable
			 * */
			for(int i = 0; i < MenuListener.projects_temp.size(); i ++) {
				if (MenuListener.choiceProject.getItemAt(MenuListener.choiceProject.getSelectedIndex()) == MenuListener.projects_temp.get(i)) {
					 index = MenuListener.project_index.get(i);
				}
			}
			
			// updating selected item with finalizing information
			((Project) Application.container.get(index)).setTotalFee(MenuListener.totalFee_TF.getText());
			
			// Generation of invoice object
			Invoice invoice = new Invoice(((Project) Application.container.get(index)).getClient().getName(),
					((Project) Application.container.get(index)).getClient().getPhone(),
					((Project) Application.container.get(index)).getClient().getEmail(),
					((Project) Application.container.get(index)).getTotalFee(),
					((Project) Application.container.get(index)).getPaidToDate());
			
			// updating selected item with finalizing information
			((Project) Application.container.get(index)).setFinalized(true);
			((Project) Application.container.get(index)).setInvoice(invoice);
			((Project) Application.container.get(index)).setCompletedOn(MenuListener.completionDate_TF.getText());
			
			
		}
		// Return to main menu
		Application.main(null);
	}
	
}