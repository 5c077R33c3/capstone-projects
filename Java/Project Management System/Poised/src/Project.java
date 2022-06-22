package project.Poised;

public class Project {
	/*
	 * This class generates a Project object which then contains information regarding each project
	 */
	
	// Class variable declaration
	private String projectNumber;
	private String projectName;
	private String building;
	private String address;
	private String ERF;
	private String totalFee;
	private String paidToDate;
	private String deadline;
	private Person architect;
	private Person contractor;
	private Person client;
	private Invoice invoice;
	private boolean finalized;
	private String completedOn;
	
	// Project constructor
	public Project(String projectNumber, String projectName, String building, String address, String ERF,
			Person architect, Person contractor, Person client) {
		
		this.projectNumber = projectNumber;
		this.projectName = projectName;
		this.building = building;
		this.address = address;
		this.ERF = ERF;
		this.architect = architect;
		this.contractor = contractor;
		this.client = client;
		this.setFinalized(false);
	}
	
	// Getters and Setters for Class Variables
	
	public String getProjectNumber() {
		return projectNumber;
	}
	public void setProjectNumber(String projectNumber) {
		this.projectNumber = projectNumber;
	}
	public String getProjectName() {
		return projectName;
	}
	public void setProjectName(String projectName) {
		this.projectName = projectName;
	}
	public String getBuilding() {
		return building;
	}
	public void setBuilding(String building) {
		this.building = building;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getERF() {
		return ERF;
	}
	public void setERF(String eRF) {
		ERF = eRF;
	}
	public String getTotalFee() {
		return totalFee;
	}
	public void setTotalFee(String totalFee) {
		this.totalFee = totalFee;
	}
	public String getPaidToDate() {
		return paidToDate;
	}
	public void setPaidToDate(String paidToDate) {
		this.paidToDate = paidToDate;
	}
	public String getDeadline() {
		return deadline;
	}
	public void setDeadline(String deadline) {
		this.deadline = deadline;
	}
	public Person getArchitect() {
		return architect;
	}
	public void setArchitect(Person architect) {
		this.architect = architect;
	}
	public Person getContractor() {
		return contractor;
	}
	public void setContractor(Person contractor) {
		this.contractor = contractor;
	}
	public Person getClient() {
		return client;
	}
	public void setClient(Person client) {
		this.client = client;
	}

	public boolean isFinalized() {
		return finalized;
	}

	public void setFinalized(boolean finalized) {
		this.finalized = finalized;
	}

	public String getCompletedOn() {
		return completedOn;
	}

	public void setCompletedOn(String completedOn) {
		this.completedOn = completedOn;
	}

	public Invoice getInvoice() {
		return invoice;
	}

	public void setInvoice(Invoice invoice) {
		this.invoice = invoice;
	}
	


}
