window.nativeHlsError = function(videoEl){
  // Burada istersen kullanıcıya daha açıklayıcı bir modal gösterebilirsin
  console.warn("Tarayıcı HLS oynatmada sorun yaşıyor:", videoEl?.error);
};
