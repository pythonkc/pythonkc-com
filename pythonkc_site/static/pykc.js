var pykc = window.pykc = pykc || {};
pykc.map;

pykc.mapInit = function(lat,lon) {
    var latlng = new google.maps.LatLng(lat,lon);
    var opts = {
        zoom: 14,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    this.map = new google.maps.Map(document.getElementById("map_canvas"), opts);
    var venue = new google.maps.Marker({
        position: latlng, 
        map: this.map
    });
}

pykc.resizeMap = function(){
    this.$mapHolder = this.$mapHolder || $("#map_canvas");
    this.$mapHolder.width( this.$mapHolder.parent().width()/2);
    google.maps.event.trigger(this.map, 'resize');
}

pykc.$slides = $('#evt-wrapper').children();
pykc.slideNum = 0;

pykc.onPrev = function(e){
    var $ele = pykc.$slides.eq(pykc.slideNum-1);
    var eloffset = $ele.position().left;
    e.preventDefault();
    if (pykc.slideNum === 0) return;
    eloffset === 0 ?
        pykc.$slides.parent().animate({left: 0}) :
        pykc.$slides.parent().animate({left: '+='+eloffset})
    pykc.slideNum --;
    pykc.checkButtons('prev');
}

pykc.onNext = function(e){
    e.preventDefault();
    if (pykc.slideNum === pykc.$slides.length-1) return;
    var $ele = pykc.$slides.eq(pykc.slideNum+1);
    var eloffset = $ele.position().left;
    pykc.$slides.parent().animate({left: -eloffset});
    pykc.slideNum ++;
    pykc.checkButtons('next');
}

pykc.checkButtons = function(id){
    if ( pykc.slideNum === 0 || pykc.slideNum === pykc.$slides.length-1) {
        $('#'+id).addClass('disabled');
    }else{
        $('.btn-control').removeClass('disabled');
    }
}

pykc.init = function(lat,lon){
    $('.top').click(function(e){
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, 300);
    });
    $('#prev').click(pykc.onPrev);
    $('#next').click(pykc.onNext);
    this.mapInit(lat,lon);
    this.resizeMap();
}

