$(document).ready(function() {
    $('#loginForm').on('submit', function(event) {
        event.preventDefault(); // 기본 폼 제출 방지

        const nickname = $('#nicknameInput').val();
        const password = $('#passwordInput').val();

        // 비밀번호 유효성 검사
        if (password.length < 4 ) {
            return; // 비밀번호가 유효하지 않으면 제출하지 않음
        }

        $.ajax({
            url: '/way/signin', // 로그인 엔드포인트
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ nickname: nickname, password: password }),
            success: function(response) {
                if (response.status === 'success') {
                    // 로그인 성공시 홈 페이지로 리다이렉트
                    window.location.href = '/way';
                } else {
                    // 로그인 실패시 오류 메시지 표시
                    alert('로그인 실패: ' + response.message);
                }
            },
            error: function(error) {
                console.error('Error:', error);
                alert('로그인 요청 중 오류가 발생했습니다.');
            }
        });
    });
});
