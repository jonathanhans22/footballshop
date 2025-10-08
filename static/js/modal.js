// ======================================================
//          LOGIKA UNTUK MODAL REUSABLE
// ======================================================

const modal = document.getElementById('universal-modal');
const modalOverlay = document.getElementById('modal-overlay');
const modalContent = document.getElementById('modal-content');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');
const modalFooter = document.getElementById('modal-footer');

/**
 * Menampilkan modal dengan konten yang dinamis.
 * @param {object} options - Opsi untuk modal.
 * @param {string} options.title - Judul yang akan ditampilkan di header modal.
 * @param {string} options.bodyHtml - Konten HTML untuk body modal.
 * @param {string} [options.footerHtml] - Konten HTML untuk footer modal (tombol-tombol).
 */
function openModal({ title, bodyHtml, footerHtml }) {
    modalTitle.textContent = title;
    modalBody.innerHTML = bodyHtml;

    if (footerHtml) {
        modalFooter.innerHTML = footerHtml;
    } else {
        // Default footer jika tidak disediakan
        modalFooter.innerHTML = `<button type="button" class="px-6 py-2 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50" onclick="closeModal()">Tutup</button>`;
    }

    // Tampilkan modal dengan animasi
    modal.classList.remove('opacity-0', 'pointer-events-none');
    modalContent.classList.remove('scale-95', 'opacity-0');
    
    // Tambahkan event listener untuk menutup modal saat klik overlay atau Esc
    modalOverlay.addEventListener('click', closeModal);
    document.addEventListener('keydown', handleEscKey);
}

// Fungsi untuk menutup modal
function closeModal() {
    // Sembunyikan modal dengan animasi
    modal.classList.add('opacity-0');
    modalContent.classList.add('scale-95', 'opacity-0');
    
    // Tunggu animasi selesai sebelum menonaktifkan pointer events
    setTimeout(() => {
        modal.classList.add('pointer-events-none');
    }, 300); // Durasi harus sama dengan durasi transisi di CSS

    // Hapus event listener
    modalOverlay.removeEventListener('click', closeModal);
    document.removeEventListener('keydown', handleEscKey);
}

// Handler untuk tombol Escape
function handleEscKey(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
}


// --- CONTOH PENGGUNAAN ---

// 1. Contoh untuk Konfirmasi Hapus
function showDeleteConfirmation(productName, deleteUrl) {
    openModal({
        title: `Hapus Produk: ${productName}?`,
        bodyHtml: `<p class="text-gray-600">Apakah Anda yakin ingin menghapus produk ini secara permanen? Tindakan ini tidak dapat diurungkan.</p>`,
        footerHtml: `
            <button type="button" class="px-6 py-2 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50" onclick="closeModal()">
                Batal
            </button>
            <a href="${deleteUrl}" class="px-6 py-2 bg-red-600 text-white rounded-md font-medium hover:bg-red-700 ml-3">
                Ya, Hapus
            </a>
        `
    });
}

// 2. Contoh untuk Menampilkan Form dari Template Lain (Lebih Canggih)
async function showCreateFormInModal() {
    // Anda bisa fetch konten form dari URL Django yang hanya merender bagian form
    // const response = await fetch('/get-create-form-template/');
    // const formHtml = await response.text();

    const formHtml = `
        <form id="product-form-modal">
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Nama Produk</label>
                <input type="text" id="name" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2">
            </div>
             <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Harga</label>
                <input type="number" id="price" class="mt-1 block w-full border border-gray-300 rounded-md px-3 py-2">
            </div>
        </form>
    `;

    openModal({
        title: 'Tambah Produk Baru',
        bodyHtml: formHtml,
        footerHtml: `
            <button type="button" class="px-6 py-2 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50" onclick="closeModal()">Batal</button>
            <button type="submit" form="product-form-modal" class="px-6 py-2 bg-green-600 text-white rounded-md font-medium hover:bg-green-700 ml-3">Simpan</button>
        `
    });
}

// Untuk menggunakan contoh di atas, Anda bisa menambahkan tombol di HTML Anda:
// <button onclick="showDeleteConfirmation('Bola Adidas', '/delete/123')">Hapus Produk</button>
// <button onclick="showCreateFormInModal()">Tambah via Modal</button>