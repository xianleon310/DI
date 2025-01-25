package com.example.firebase2ev.models;

public class User {
    private String id,address,fullname,phone,email;

    public User(){}
    public User(String id,String address,String fullname,String phone,String email){
        this.id=id;
        this.address=address;
        this.fullname=fullname;
        this.phone=phone;
        this.email=email;
    }
    public String getId(){return id;}
    public String getAddress(){return address;}
    public String getFullname(){return fullname;}
    public String getPhone(){return phone;}
    public String getEmail(){return email;}
}
