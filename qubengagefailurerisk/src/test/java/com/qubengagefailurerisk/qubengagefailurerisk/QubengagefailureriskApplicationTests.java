package com.qubengagefailurerisk.qubengagefailurerisk;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;

@SpringBootTest
@AutoConfigureMockMvc
public class QubengagefailureriskApplicationTests {

	@Autowired
	private MockMvc mockMvc;

	@Test
	public void whenEngagementScoreBelowCutOff_thenReturnAtRisk() throws Exception {
		this.mockMvc.perform(get("/check_risk")
				.param("engagementScore", "0.50") // Pass the score as a decimal
				.param("cutOff", "60"))
				.andExpect(status().isOk())
				.andExpect(jsonPath("$.studentFailureRisk").value("Student is at risk of failure."));
	}

	@Test
	public void whenEngagementScoreAboveCutOff_thenReturnNotAtRisk() throws Exception {
		this.mockMvc.perform(get("/check_risk")
				.param("engagementScore", "0.70")
				.param("cutOff", "60"))
				.andExpect(status().isOk())
				.andExpect(jsonPath("$.studentFailureRisk").value("Student is not at risk of failure."));
	}

	@Test
	public void whenInvalidParameters_thenThrowException() throws Exception {
		this.mockMvc.perform(get("/check_risk")
				.param("engagementScore", "not_a_number")
				.param("cutOff", "60"))
				.andExpect(status().isBadRequest());
	}
}
