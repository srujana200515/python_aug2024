document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.querySelector('.hero .btn');
    const authModal = document.getElementById('authModal');
    const loginForm = document.querySelector('.login-form');
    const registerForm = document.querySelector('.register-form');
    const toggleFormLinks = document.querySelectorAll('.toggle-form');
    const closeBtn = document.querySelector('.close-btn');
    const loginFormElement = document.getElementById('loginForm');
    const registerFormElement = document.getElementById('registerForm');

    // Show modal function with improved visibility
    function showAuthModal() {
        authModal.style.display = 'block';
        authModal.classList.add('show');
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
    }

    // Close modal function with improved transition
    function closeAuthModal() {
        authModal.classList.remove('show');
        setTimeout(() => {
            authModal.style.display = 'none';
        }, 300);
    }

    // Toggle between login and register forms
    toggleFormLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            loginForm.classList.toggle('active');
            registerForm.classList.toggle('active');
        });
    });

    // Close modal when clicking outside
    window.addEventListener('click', (event) => {
        if (event.target === authModal) {
            closeAuthModal();
        }
    });

    // Close button functionality
    closeBtn.addEventListener('click', closeAuthModal);

    // Validation functions
    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function validatePassword(password) {
        return password.length >= 8 && 
               /[A-Z]/.test(password) && 
               /[a-z]/.test(password) && 
               /[0-9]/.test(password);
    }

    function validatePhoneNumber(phone) {
        const phoneRegex = /^[6-9]\d{9}$/;
        return phoneRegex.test(phone);
    }

    // Login form submission with enhanced validation
    loginFormElement.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value.trim();
        const password = document.getElementById('loginPassword').value;

        if (!validateEmail(email)) {
            alert('Please enter a valid email address');
            return;
        }

        if (!validatePassword(password)) {
            alert('Password must be at least 8 characters long and contain uppercase, lowercase, and number');
            return;
        }

        // Simulated login (replace with actual authentication)
        try {
            // Placeholder for actual authentication logic
            console.log('Login attempt:', email);
            alert('Login Successful!');
            closeAuthModal();
        } catch (error) {
            alert('Login failed. Please try again.');
        }
    });

    // Registration form submission with comprehensive validation
    registerFormElement.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('registerName').value.trim();
        const email = document.getElementById('registerEmail').value.trim();
        const phone = document.getElementById('registerPhone').value.trim();
        const password = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        // Validate each field
        if (name.length < 2) {
            alert('Please enter a valid name');
            return;
        }

        if (!validateEmail(email)) {
            alert('Please enter a valid email address');
            return;
        }

        if (!validatePhoneNumber(phone)) {
            alert('Please enter a valid 10-digit Indian mobile number');
            return;
        }

        if (!validatePassword(password)) {
            alert('Password must be at least 8 characters long and contain uppercase, lowercase, and number');
            return;
        }

        if (password !== confirmPassword) {
            alert('Passwords do not match');
            return;
        }

        // Simulated registration (replace with actual registration logic)
        try {
            // Placeholder for actual registration logic
            console.log('Registration attempt:', { name, email, phone });
            alert('Registration Successful!');
            closeAuthModal();
        } catch (error) {
            alert('Registration failed. Please try again.');
        }
    });

    // Expose showAuthModal to global scope
    window.showAuthModal = showAuthModal;
});