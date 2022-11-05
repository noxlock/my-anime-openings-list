(function(t){function e(e){for(var r,o,i=e[0],c=e[1],l=e[2],d=0,f=[];d<i.length;d++)o=i[d],Object.prototype.hasOwnProperty.call(n,o)&&n[o]&&f.push(n[o][0]),n[o]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);u&&u(e);while(f.length)f.shift()();return s.push.apply(s,l||[]),a()}function a(){for(var t,e=0;e<s.length;e++){for(var a=s[e],r=!0,i=1;i<a.length;i++){var c=a[i];0!==n[c]&&(r=!1)}r&&(s.splice(e--,1),t=o(o.s=a[0]))}return t}var r={},n={index:0},s=[];function o(e){if(r[e])return r[e].exports;var a=r[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.m=t,o.c=r,o.d=function(t,e,a){o.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},o.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},o.t=function(t,e){if(1&e&&(t=o(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)o.d(a,r,function(e){return t[e]}.bind(null,r));return a},o.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return o.d(e,"a",e),e},o.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},o.p="";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=e,i=i.slice();for(var l=0;l<i.length;l++)e(i[l]);var u=c;s.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("4570")},"01e3":function(t,e,a){"use strict";a("9f03")},2202:function(t,e,a){t.exports=a.p+"img/ai-art-3.png"},2734:function(t,e,a){t.exports=a.p+"img/ai-art-1.png"},3693:function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-sheet",{staticClass:"mx-auto",attrs:{elevation:"8","max-width":"100%"}},[a("v-slide-group",{staticClass:"pa-4",attrs:{"show-arrows":""},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}},t._l(t.songs,(function(e){return a("v-slide-item",{key:e.pk,scopedSlots:t._u([{key:"default",fn:function(t){var r=t.active,n=t.toggle;return[a("v-card",{staticClass:"ma-4",attrs:{color:r?"primary":"grey lighten-1",height:"200",width:"134"},on:{click:n}},[a("v-row",{staticClass:"fill-height",attrs:{align:"center",justify:"center"}},[a("v-img",{attrs:{src:e.anime__cover}})],1)],1)]}}],null,!0)})})),1),a("v-expand-transition",[null!=t.selected?a("v-sheet",{attrs:{height:"400",tile:""}},[a("v-row",{staticClass:"fill-height",staticStyle:{"background-color":"lightgray"},attrs:{align:"center",justify:"center"}},[a("video",{attrs:{controls:"",width:"35%",preload:"auto"}},[a("source",{attrs:{src:t.selectedSong.video_link,type:"video/webm"}})]),a("div",{staticStyle:{"padding-left":"15em",color:"blue"}},[a("a",{attrs:{href:t.selectedSong.detail_link}},[a("h3",[t._v(" "+t._s(t.selectedSong.anime__english_name+" "+t.selectedSong.song_type+t.selectedSong.number)+" "),a("br")]),a("h4",[t._v(" "+t._s(t.selectedSong.name)+" ")])]),a("br"),a("v-select",{attrs:{items:[1,2,3,4,5,6,7,8,9,10],label:"Rating","return-object":"",filled:!0},model:{value:t.rating,callback:function(e){t.rating=e},expression:"rating"}}),t.user==t.username?a("v-btn",{attrs:{color:"primary",disabled:""}},[t._v(" Song already in list ")]):a("v-btn",{attrs:{color:"primary",disabled:""===t.rating},on:{click:function(e){return t.addToList(t.selectedSong.pk)}}},[t._v(" Add To List ")])],1)])],1):t._e()],1),a("v-snackbar",{attrs:{timeout:2e3,color:t.snackColour},scopedSlots:t._u([{key:"action",fn:function(e){var r=e.attrs;return[a("v-btn",t._b({attrs:{text:""},on:{click:function(e){t.snack=!1}}},"v-btn",r,!1),[t._v(" Close ")])]}}]),model:{value:t.snack,callback:function(e){t.snack=e},expression:"snack"}},[t._v(" "+t._s(t.snackText)+" ")])],1)},n=[],s={name:"Carousel",props:{songs:{type:Array},user:{type:String},username:{type:String}},data:function(){return{selected:null,rating:"",snack:"",snackText:"",snackColour:""}},methods:{addToList:function(t){var e=this;this.$http.post("/api/addtolist/",{method:"POST",data:{song:t,rating:this.rating}}).then((function(t){201===t.status?(e.snack=!0,e.snackColour="success",e.snackText="Song added successfully!"):(e.snack=!0,e.snackColour="error",e.snackText="This song is already in your list!")})).catch((function(){e.snack=!0,e.snackColour="error",e.snackText="An unknown error has occurred"}))}},computed:{selectedSong:function(){return this.songs[this.selected]}},mounted:function(){this.$http.defaults.xsrfHeaderName="X-CSRFToken",this.$http.defaults.xsrfCookieName="csrftoken"}},o=s,i=a("2877"),c=Object(i["a"])(o,r,n,!1,null,null,null);e["a"]=c.exports},"402c":function(t,e,a){"use strict";var r=a("a026"),n=a("ce5b"),s=a.n(n);a("bf40");r["default"].use(s.a);var o={};e["a"]=new s.a(o)},4046:function(t,e,a){"use strict";a("8ce7")},4570:function(t,e,a){"use strict";a.r(e);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("a026"),n=a("bc3a"),s=a.n(n),o=a("130e"),i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-main",[a("ToolBar",{attrs:{user:t.username}}),a("HomeAppBar"),a("BannerCarousel",{attrs:{height:"500",heading:"MAOL",subheader:"The best anime site since "+t.date.toLocaleString()}}),a("v-card",{staticClass:"text-h4",attrs:{outlined:""}},[t._v("Top Songs")]),a("Carousel",{attrs:{songs:t.songs}})],1)},c=[],l=a("d546"),u=a("a763"),d=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-carousel",{attrs:{cycle:"",height:"400","hide-delimiter-background":"","show-arrows-on-hover":""}},[r("v-carousel-item",[r("v-parallax",{staticClass:"artone",attrs:{dark:"",src:a("2734"),height:t.height}},[r("div",{staticClass:"bannertext-background"},[r("h1",{staticClass:"banner-header text-h4 mb-4 text-center"},[t._v(" "+t._s(t.heading)+" ")]),r("h4",{staticClass:"subheading text-center"},[t._v(" "+t._s(t.subheader)+" ")])])])],1),r("v-carousel-item",[r("v-parallax",{staticClass:"arttwo",attrs:{dark:"",src:a("fe11"),height:t.height}},[r("div",{staticClass:"bannertext-background"},[r("h1",{staticClass:"banner-header text-h4 mb-4 text-center"},[t._v(" "+t._s(t.heading)+" ")]),r("h4",{staticClass:"subheading text-center"},[t._v(" "+t._s(t.subheader)+" ")])])])],1),r("v-carousel-item",[r("v-parallax",{staticClass:"artthree",attrs:{dark:"",src:a("2202"),height:t.height}},[r("div",{staticClass:"bannertext-background"},[r("h1",{staticClass:"banner-header text-h4 mb-4 text-center"},[t._v(" "+t._s(t.heading)+" ")]),r("h4",{staticClass:"subheading text-center"},[t._v(" "+t._s(t.subheader)+" ")])])])],1)],1)},f=[],h={name:"BannerCarousel",props:{styles:{type:String},image:{type:String},height:{type:String},heading:{type:String},subheader:{type:String}},data:function(){return{}}},p=h,v=(a("4046"),a("2877")),g=Object(v["a"])(p,d,f,!1,null,"0e59fd55",null),m=g.exports,b=a("3693"),y={name:"Home",components:{ToolBar:l["a"],HomeAppBar:u["a"],BannerCarousel:m,Carousel:b["a"]},props:{songs:{type:Array},username:{type:String}},data:function(){return{date:new Date(Date.now())}}},_=y,x=(a("01e3"),Object(v["a"])(_,i,c,!1,null,null,null)),k=x.exports,C=a("402c");r["default"].config.productionTip=!1,r["default"].use(o["a"],s.a),new r["default"]({vuetify:C["a"],el:"#app",components:{Home:k}})},"497b":function(t,e,a){"use strict";a("efaa")},"8ce7":function(t,e,a){},"91b8":function(t,e,a){"use strict";a("cac7")},"9f03":function(t,e,a){},a763:function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-card",[a("v-tabs",{staticClass:"d-flex justify-center",attrs:{"hide-slider":""}},[a("v-tab",{staticClass:"home",attrs:{href:"/"}},[t._v(" Home ")]),a("v-tab",{attrs:{href:"/anime"}},[t._v(" Anime ")]),a("v-tab",{attrs:{href:"/top"}},[t._v(" Top ")]),a("v-tab",{attrs:{href:"/random"}},[t._v(" Random ")]),a("form",{attrs:{id:"search",action:"/search"}},[a("v-text-field",{staticClass:"search mt-1",class:{closed:t.searchClosed&&!t.query},attrs:{id:"query",name:"q",type:"search",placeholder:"Search",filled:"",dense:"","prepend-inner-icon":"mdi-magnify"},on:{focus:function(e){t.searchClosed=!1},blur:function(e){t.searchClosed=!0}},model:{value:t.query,callback:function(e){t.query=e},expression:"query"}})],1)],1)],1)},n=[],s={name:"HomeAppBar",props:{},data:function(){return{searchClosed:!0,query:null}}},o=s,i=(a("497b"),a("2877")),c=Object(i["a"])(o,r,n,!1,null,null,null);e["a"]=c.exports},cac7:function(t,e,a){},d546:function(t,e,a){"use strict";var r=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-card",{attrs:{elevation:"0"}},[a("v-toolbar",{attrs:{flat:""}},[a("a",{attrs:{href:"/"}},[a("v-img",{attrs:{src:"/static/site-logo-trans.png","max-width":"267","max-height":"63"}})],1),a("v-spacer"),a("div",{staticClass:"d-flex justify-space-between"},[a("div",["AnonymousUser"!=t.user?a("a",{attrs:{href:"/profile/"+t.user}},[t._v(" "+t._s(t.user)+" "),a("v-icon",[t._v("mdi-account")])],1):a("a",{attrs:{href:"/auth/login"}},[t._v("Login")])]),a("br"),a("a",{attrs:{href:"/auth/logout"}},[a("v-icon",[t._v("mdi-exit-to-app")])],1)])],1)],1)},n=[],s={name:"Toolbar",props:{user:{type:String}}},o=s,i=(a("91b8"),a("2877")),c=Object(i["a"])(o,r,n,!1,null,"0f36f594",null);e["a"]=c.exports},efaa:function(t,e,a){},fe11:function(t,e,a){t.exports=a.p+"img/ai-art-2.png"}});