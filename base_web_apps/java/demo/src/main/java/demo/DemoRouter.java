package demo;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMethod;

@RestController
public class DemoRouter{

  @RequestMapping(value="/home", method=RequestMethod.GET)
  public String viewHome(){
      return "home";
  }
  @RequestMapping(value="/", method=RequestMethod.GET)
  public String viewDefault(){
    return "home";
  }
  @RequestMapping(value="/index", method=RequestMethod.GET)
  public String viewIndex(){
      return "home";
  }

}
