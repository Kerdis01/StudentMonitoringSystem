package main

import (
	"encoding/json"
	"log"
	"net/http"
	"strconv"
)

// Struct for the response data
type ResponseData struct {
	AverageHours float64 `json:"average_hours"`
}

func main() {
	http.HandleFunc("/calculate_average_hours", calculateAverageHoursHandler)
	log.Fatal(http.ListenAndServe(":8090", nil))
}

func calculateAverageHoursHandler(w http.ResponseWriter, r *http.Request) {
	// Enable CORS
	enableCors(&w)

	// Only allow GET requests
	if r.Method != "GET" {
		http.Error(w, "Method is not supported.", http.StatusNotFound)
		return
	}

	// Get the total_hours parameter from URL
	totalHoursStr := r.URL.Query().Get("total_hours")
	if totalHoursStr == "" {
		http.Error(w, "total_hours parameter is missing", http.StatusBadRequest)
		return
	}

	totalHours, err := strconv.ParseFloat(totalHoursStr, 64)
	if err != nil {
		http.Error(w, "Invalid total_hours value", http.StatusBadRequest)
		return
	}

	// Calculate average hours
	averageHours := totalHours / 4

	// Create response data
	responseData := ResponseData{
		AverageHours: averageHours,
	}

	// Send response back
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(responseData)
}

func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
	(*w).Header().Set("Access-Control-Allow-Methods", "GET, OPTIONS")
	(*w).Header().Set("Access-Control-Allow-Headers", "Content-Type")
}
