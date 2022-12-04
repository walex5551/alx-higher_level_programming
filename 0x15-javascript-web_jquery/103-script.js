window.addEventListener('DOMContentLoaded', function () {
  $('input#language_code').keypress(function (event) {
    var code = event.keycode || event.which;
    if (code === 13) {
      const lang = $('input#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
  $('input#btn_translate').click(function () {
    const lang = $('input#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
