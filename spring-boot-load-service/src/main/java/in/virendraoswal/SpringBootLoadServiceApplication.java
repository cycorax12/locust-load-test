package in.virendraoswal;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class SpringBootLoadServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootLoadServiceApplication.class, args);
	}

}

@RestController
class RandomResource {

	@GetMapping(value = "/greet")
	public String greet() {
		return "Locust Load Test.";
	}
}
