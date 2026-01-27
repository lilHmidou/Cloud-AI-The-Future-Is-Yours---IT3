output "public_ip" {
  description = "The public IP address of the instance"
  value       = google_compute_address.public_ip["web"].address
}