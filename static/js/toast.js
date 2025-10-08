// ======================================================
//          LOGIKA UNTUK TOAST NOTIFICATION
// ======================================================

const toastElement = document.getElementById('toast-notification');
const toastIconContainer = document.getElementById('toast-icon-container');
const toastTitle = document.getElementById('toast-title');
const toastMessage = document.getElementById('toast-message');

// Variabel untuk timeout agar bisa di-clear
let toastTimeout;

// Konfigurasi untuk setiap tipe notifikasi
const toastTypes = {
    success: {
        bgClass: 'bg-green-600',
        icon: '✔️'
    },
    error: {
        bgClass: 'bg-red-600',
        icon: '✖️'
    },
    warning: {
        bgClass: 'bg-yellow-500',
        icon: '⚠️'
    },
    info: {
        bgClass: 'bg-blue-600',
        icon: 'ℹ️'
    }
};

/**
 * Menampilkan toast notification.
 * @param {object} options - Opsi untuk toast.
 * @param {('success'|'error'|'warning'|'info')} options.type - Tipe notifikasi.
 * @param {string} options.title - Judul notifikasi.
 * @param {string} options.message - Pesan notifikasi.
 * @param {number} [options.duration=5000] - Durasi dalam milidetik.
 */
function showToast({ type, title, message, duration = 5000 }) {
    // Hapus timeout sebelumnya jika ada
    clearTimeout(toastTimeout);

    // Hapus kelas warna sebelumnya
    Object.values(toastTypes).forEach(t => toastElement.classList.remove(t.bgClass));

    // Dapatkan konfigurasi berdasarkan tipe
    const config = toastTypes[type] || toastTypes.info;

    // Set konten dan gaya
    toastElement.classList.add(config.bgClass);
    toastIconContainer.innerHTML = `<span>${config.icon}</span>`;
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Tampilkan toast
    toastElement.classList.remove('opacity-0', 'translate-y-10');

    // Sembunyikan otomatis setelah durasi tertentu
    toastTimeout = setTimeout(() => {
        hideToast();
    }, duration);
}

// Fungsi untuk menyembunyikan toast
function hideToast() {
    toastElement.classList.add('opacity-0', 'translate-y-10');
    clearTimeout(toastTimeout);
}

// CONTOH PENGGUNAAN (bisa dipanggil dari template lain):
// showToast({
//     type: 'success',
//     title: 'Berhasil!',
//     message: 'Produk berhasil ditambahkan ke keranjang.'
// });
// showToast({
//     type: 'error',
//     title: 'Gagal!',
//     message: 'Tidak dapat terhubung ke server.'
// });