document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');
    const ratingInput = document.getElementById('rating');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            ratingInput.value = value;
            updateStars(value);
        });

        star.addEventListener('mouseover', function() {
            const value = this.getAttribute('data-value');
            updateStars(value);
        });

        star.addEventListener('mouseout', function() {
            const value = ratingInput.value;
            updateStars(value);
        });
    });

    function updateStars(value) {
        stars.forEach(star => {
            const starValue = star.getAttribute('data-value');
            if (starValue <= value) {
                star.textContent = '★';
                star.classList.add('active');
            } else {
                star.textContent = '☆';
                star.classList.remove('active');
            }
        });
    }

    // 初始化显示
    updateStars(ratingInput.value);
}); 