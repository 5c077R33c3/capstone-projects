package project.Poised;

public class Person {
	
	String name; 
	String phone;
	String email; 
	String address;
	String title;
	
	public Person(String name, String phone, String email, String address, String title) {
		
		this.name = name;
		this.phone = phone;
		this.email = email;
		this.address = address;
		this.title = title;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}


}
