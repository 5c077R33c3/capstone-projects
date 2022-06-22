package project.Poised;

public class Invoice {
	
	private String client;
	private String client_phone;
	private String client_email;
	private Integer fee;
	private Integer paidToDate;
	private Integer toPay;
	
	public Invoice(String client, String client_phone, String client_email, String fee, String paidToDate) {
		
		this.client = client;
		this.client_phone = client_phone;
		this.client_email = client_email;
		this.fee = Integer.parseInt(fee);
		this.paidToDate = Integer.parseInt(paidToDate);
		this.toPay = Integer.parseInt(fee) - Integer.parseInt(paidToDate);
		
		
	}
	
	public String generateInvoice() {
		String Invoice = client +"\n"
				+ "Phone: " + client_phone + "\n"
				+ "Email: " + client_email + "\n"
				+ "Total = " + Integer.toString(toPay);
		return Invoice;
		
	}

}
