package com.mycompany.examplejavaapp.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


/**
 *
 * @author koalatea
 */
@Controller
public class HomeController {
    
    @RequestMapping(value="/home", method=RequestMethod.GET)
    public String viewHome(){
        return "home";
    }
}
