resource "google_compute_network" "vpc" {
  name                    = "${var.ssh_user}-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.ssh_user}-subnet"
  region        = var.region
  ip_cidr_range = "10.10.0.0/24"
  network       = google_compute_network.vpc.id
}

resource "google_compute_firewall" "allow_ssh" {
  name    = "${var.ssh_user}-ssh"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["demo-ssh"]
}

resource "google_compute_firewall" "allow_web" {
  name    = "${var.ssh_user}-web"
  network = google_compute_network.vpc.name

  allow {
    protocol = "tcp"
    ports    = [tostring(var.web_port)]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["demo-web"]
}