package demo;

import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class DemoRouter{

	private String message = "Hello World";

  @RequestMapping(value="/", method=RequestMethod.GET)
  public String viewDefault(Map<String, Object> model){
    model.put("message", this.message);
    return "index";
  }

  @RequestMapping(value="/add", method=RequestMethod.GET)
  public String ViewAdd(){
    return "add";
  }

  @RequestMapping(value="/add", method=RequestMethod.POST)
  public String AddSubmit(@RequestParam("data") String data){
    if(data != null && !data.isEmpty()) {
      return "added";
    }
    return "failed";
  }

}
