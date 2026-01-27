resource "google_compute_address" "static_ip" {
  name = "nginx-static-ip"
}

resource "google_compute_instance" "nginx_vm" {
  name         = "nginx-vm"
  machine_type = "e2-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-12-bookworm-v20240515"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet.id

    access_config {
      nat_ip = google_compute_address.static_ip.address
    }
  }

  metadata = {
    ssh-keys = "${var.ssh_user}:${file("~/.ssh/id_ed25519.pub")}"
  }
}
