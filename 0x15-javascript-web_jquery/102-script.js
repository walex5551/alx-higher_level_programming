window.addEventListener('DOMContentLoaded', function () {
  $('INPUT').eq(1).click(function () {
    const lang = $('INPUT').eq(0).val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
