package com.example.firebase2ev.models;

public class Game {
    private String id,name,desc,url;
    public Game(){}
    public Game(String id,String name,String desc,String url){
        this.id=id;
        this.name=name;
        this.desc=desc;
        this.url=url;
    }

    public String getId() {return id;}

    public String getName() {return name;}

    public String getDesc() {return desc;}

    public String getUrl() {return url;}

    public void setId(String id) {this.id = id;}

    public void setName(String name){this.name=name;}

    public void setDesc(String desc){this.desc=desc;}

    public void setUrl(String url){this.desc=desc;}

}
