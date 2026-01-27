output "project_id" {
  value = "it3-terraform-tp"
}

output "public_ip" {
    value = google_compute_address.public_ip.address
}