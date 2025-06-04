# 🔐 Folder Locker (Password Protected)

A simple Python project to lock and unlock folders using a **master password**. Perfect for basic privacy protection and project-level security. Folders are hidden by renaming them and access is restricted through password verification.

## 📁 Features

- 🔑 Master password protection
- 📂 Lock/unlock any folder inside the `protected/` directory
- 🙈 Locked folders are hidden using a `.` prefix (Linux/macOS style)
- 🧠 Passwords are securely hashed (SHA-256)
- 👨‍💻 Command-line interface

## 🛠️ Technologies Used

- Python 3.x
- `getpass` – Secure password input
- `os`, `shutil` – File operations
- `hashlib` – Password hashing
- `stat` – File permissions (optional)

## 📦 Project Structure

```
file_locker/
├── config/             # Stores hashed password
│   └── hash.txt
├── protected/          # All target folders go here
│   ├── myfolder/
│   └── .myfolder/      # Locked (hidden) version
├── locker.py           # Main script
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/rahulrgit/file_locker.git
cd file_locker
```

### 2. Create Folder to Lock

```bash
mkdir protected/myfolder
```

Add your secret files inside `protected/myfolder`.

### 3. Run the Program

```bash
python3 locker.py
```

## 📷 Screenshots

```
==== FILE LOCKER ====
1. Lock Folder
2. Unlock Folder
Enter your choice: 1
Enter the folder name inside 'protected/' to target: myfolder
Enter master password:
✅ Folder 'myfolder' locked successfully.
```

## 🔒 Security Notes

- Password is stored in `config/hash.txt` as a **SHA-256 hash**
- Folder is hidden (not encrypted)
- For real security, implement encryption (e.g., using `cryptography` module)


## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! If you have feature ideas, feel free to open an issue or PR.

## 👨‍💻 Author

**Rahul Rathod**  
GitHub: [@rahulrgit](https://github.com/rahulrgit)
