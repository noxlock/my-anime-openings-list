(function(t){function e(e){for(var a,s,o=e[0],c=e[1],l=e[2],d=0,f=[];d<o.length;d++)s=o[d],Object.prototype.hasOwnProperty.call(r,s)&&r[s]&&f.push(r[s][0]),r[s]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(t[a]=c[a]);u&&u(e);while(f.length)f.shift()();return i.push.apply(i,l||[]),n()}function n(){for(var t,e=0;e<i.length;e++){for(var n=i[e],a=!0,o=1;o<n.length;o++){var c=n[o];0!==r[c]&&(a=!1)}a&&(i.splice(e--,1),t=s(s.s=n[0]))}return t}var a={},r={anime:0},i=[];function s(e){if(a[e])return a[e].exports;var n=a[e]={i:e,l:!1,exports:{}};return t[e].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.m=t,s.c=a,s.d=function(t,e,n){s.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:n})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,e){if(1&e&&(t=s(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)s.d(n,a,function(e){return t[e]}.bind(null,a));return n},s.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(e,"a",e),e},s.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},s.p="";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],c=o.push.bind(o);o.push=e,o=o.slice();for(var l=0;l<o.length;l++)e(o[l]);var u=c;i.push([4,"chunk-vendors"]),n()})({"1fcb":function(t,e,n){},3178:function(t,e,n){"use strict";n("dde9")},4:function(t,e,n){t.exports=n("42e5")},"402c":function(t,e,n){"use strict";var a=n("a026"),r=n("ce5b"),i=n.n(r);n("bf40");a["default"].use(i.a);var s={};e["a"]=new i.a(s)},"42e5":function(t,e,n){"use strict";n.r(e);n("e260"),n("e6cf"),n("cca6"),n("a79d");var a=n("a026"),r=n("bc3a"),i=n.n(r),s=n("130e"),o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-main",[n("ToolBar",{attrs:{user:t.user}}),n("HomeAppBar"),n("div",{attrs:{id:"thx"}},[n("Banner",{attrs:{styles:"anime-style",image:t.anime[0].cover,height:"150",heading:t.anime[0].english_name}})],1),n("v-row",{attrs:{"no-gutters":""}},[n("v-col",{staticClass:"left",attrs:{cols:"2"}},[n("v-card",[n("aside",[n("v-img",{attrs:{src:t.anime[0].cover}}),t._v(" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum ")],1)])],1),n("v-col",{attrs:{cols:"9"}},[n("SongList",{attrs:{ratings:t.songs,user:t.user,headers:[{text:"Type",value:"song_type"},{text:"Number",value:"number"},{text:"Song Name",value:"name"},{value:"actions",sortable:!1}]}})],1)],1)],1)},c=[],l=n("d546"),u=n("a763"),d=n("84af"),f=n("6fcc"),p={name:"Anime",components:{ToolBar:l["a"],HomeAppBar:u["a"],Banner:d["a"],SongList:f["a"]},props:{anime:{type:Array},songs:{type:Array},user:{type:String},username:{type:String}},data:function(){return{}}},v=p,m=(n("ae3a"),n("2877")),g=Object(m["a"])(v,o,c,!1,null,null,null),h=g.exports,_=n("402c");a["default"].config.productionTip=!1,a["default"].use(s["a"],i.a),new a["default"]({vuetify:_["a"],el:"#anime",components:{Anime:h}})},"497b":function(t,e,n){"use strict";n("efaa")},"6fcc":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-data-table",{staticClass:"elevation-1",attrs:{headers:t.headers,items:t.ratings,"items-per-page":-1,"hide-default-footer":""},scopedSlots:t._u([{key:"top",fn:function(){return[n("v-toolbar",{attrs:{flat:""}},[n("v-dialog",{attrs:{"max-width":"700px"},model:{value:t.playDialog,callback:function(e){t.playDialog=e},expression:"playDialog"}},[n("v-card",[n("video",{ref:"video",attrs:{src:t.videoSrc,controls:"",width:"100%",preload:"auto"}},[n("source",{attrs:{type:"video/webm"}})]),n("v-card-actions",[n("v-spacer"),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(e){return t.closeDialog("playDialog")}}},[t._v("Close ")]),n("v-spacer")],1)],1)],1),n("v-dialog",{attrs:{"max-width":"500px"},model:{value:t.addDialog,callback:function(e){t.addDialog=e},expression:"addDialog"}},[n("v-card",[n("v-card-title",{staticClass:"text-h5 justify-center"},[t._v(" Add this song to your list? ")]),n("div",{staticClass:"d-flex justify-center"},[n("v-spacer"),n("v-spacer"),n("v-select",{attrs:{items:[1,2,3,4,5,6,7,8,9,10],label:"Rating","return-object":""},model:{value:t.rating,callback:function(e){t.rating=e},expression:"rating"}}),n("v-spacer"),n("v-spacer")],1),n("v-card-actions",[n("v-spacer"),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(e){return t.closeDialog("addDialog")}}},[t._v("Cancel ")]),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(e){return t.addToList(t.selected)}}},[t._v("OK ")]),n("v-spacer")],1)],1)],1),n("v-dialog",{attrs:{"max-width":"500px"},model:{value:t.deleteDialog,callback:function(e){t.deleteDialog=e},expression:"deleteDialog"}},[n("v-card",[n("v-card-title",{staticClass:"text-h5"},[t._v(" Are you sure you want to delete this item? ")]),n("v-card-actions",[n("v-spacer"),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(e){return t.closeDialog("deleteDialog")}}},[t._v("Cancel ")]),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:t.deleteItemConfirm}},[t._v("OK ")]),n("v-spacer")],1)],1)],1)],1)]},proxy:!0},t.user==t.username?{key:"item.rating",fn:function(e){return[n("v-edit-dialog",{attrs:{"return-value":e.item.rating},on:{"update:returnValue":function(n){return t.$set(e.item,"rating",n)},"update:return-value":function(n){return t.$set(e.item,"rating",n)},open:function(n){return t.openRatingDialog(e.item)},close:function(e){return t.closeDialog("ratingDialog")}},scopedSlots:t._u([{key:"input",fn:function(){return[n("v-select",{attrs:{items:[1,2,3,4,5,6,7,8,9,10],label:"Rating","return-object":""},model:{value:t.rating,callback:function(e){t.rating=e},expression:"rating"}}),n("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(n){return t.saveRating(e.item)}}},[t._v("OK ")])]},proxy:!0}],null,!0)},[t._v(" "+t._s(e.item.rating)+" ")])]}}:null,{key:"item.song__anime__cover",fn:function(t){var e=t.item;return[n("a",{attrs:{href:"../../anime/"+e.song__anime__pk}},[n("v-img",{attrs:{contain:"","aspect-ratio":16/9,height:100,src:e.song__anime__cover}})],1)]}},{key:"item.anime__cover",fn:function(t){var e=t.item;return[n("a",{attrs:{href:"../../anime/"+e.anime__pk}},[n("v-img",{attrs:{contain:"","aspect-ratio":16/9,height:100,src:e.anime__cover}})],1)]}},{key:"item.song__anime__english_name",fn:function(e){var a=e.item;return[n("a",{attrs:{href:"../../anime/"+a.song__anime__pk}},[t._v(" "+t._s(a.song__anime__english_name)+" ")])]}},{key:"item.anime__english_name",fn:function(e){var a=e.item;return[n("a",{attrs:{href:"../../anime/"+a.anime__pk}},[t._v(" "+t._s(a.anime__english_name)+" ")])]}},{key:"item.name",fn:function(e){var a=e.item;return[n("a",{attrs:{href:a.detail_link}},[t._v(" "+t._s(a.name)+" ")])]}},{key:"item.song__name",fn:function(e){var a=e.item;return[n("a",{attrs:{href:a.song__detail_link}},[t._v(" "+t._s(a.song__name)+" ")])]}},{key:"item.actions",fn:function(e){var a=e.item;return[n("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(e){return t.playSong(a)}}},[t._v(" mdi-play-circle ")]),t.user!=t.username?n("v-icon",{staticClass:"mr-2",attrs:{small:""},on:{click:function(e){return t.openAddDialog(a)}}},[t._v(" mdi-plus-thick ")]):t._e(),t.user==t.username?n("v-icon",{attrs:{small:""},on:{click:function(e){return t.deleteItem(a)}}},[t._v(" mdi-delete ")]):t._e()]}}],null,!0)}),n("v-snackbar",{attrs:{timeout:2e3,color:t.snackColour},scopedSlots:t._u([{key:"action",fn:function(e){var a=e.attrs;return[n("v-btn",t._b({attrs:{text:""},on:{click:function(e){t.snack=!1}}},"v-btn",a,!1),[t._v(" Close ")])]}}]),model:{value:t.snack,callback:function(e){t.snack=e},expression:"snack"}},[t._v(" "+t._s(t.snackText)+" ")])],1)},r=[],i=(n("a434"),{name:"SongList",components:{},props:{user:{type:String},username:{type:String,default:"system"},ratings:{type:Array},headers:{type:Array}},data:function(){return{snack:"",snackText:"",snackColour:"",deleteDialog:!1,playDialog:!1,addDialog:!1,expanded:[],index:-1,rating:"",videoSrc:"",selected:null}},watch:{playDialog:function(t){t||this.$refs.video.pause()}},methods:{addToList:function(t){var e=this;t=t.pk?t.pk:t.song__pk,this.$http.post("/api/addtolist/",{method:"POST",data:{song:t,rating:this.rating}}).then((function(t){201===t.status?(e.snack=!0,e.snackColour="success",e.snackText="Song added successfully!"):(e.snack=!0,e.snackColour="error",e.snackText="This song is already in your list!")})).catch((function(){e.snack=!0,e.snackColour="error",e.snackText="An unknown error has occurred"}))},editRating:function(t){var e=this;this.$http.post("/api/editrating/",{method:"POST",data:{song:t,new_rating:this.rating}}).then((function(){e.snack=!0,e.snackColour="success",e.snackText="Rating updated successfully! Refresh to update."})).catch((function(){e.snack=!0,e.snackColour="error",e.snackText="An unknown error has occurred."}))},removeFromList:function(t){var e=this;t=t.pk?t.pk:t.song__pk,this.$http.post("/api/deletefromlist/",{method:"POST",data:{song:t}}).then((function(){e.ratings.splice(e.index,1),e.snack=!0,e.snackColour="success",e.snackText="Song deleted successfully!"})).catch((function(){e.snack=!0,e.snackColour="error",e.snackText="An unknown error has occurred"}))},playSong:function(t){t.video_link?this.selected=t.video_link:this.selected=t.song__video_link,this.playDialog=!0,this.videoSrc=this.selected},deleteItem:function(t){this.selected=t,this.index=this.ratings.indexOf(t),this.deleteDialog=!0},deleteItemConfirm:function(){this.removeFromList(this.selected),this.closeDialog("deleteDialog")},saveRating:function(t){this.editRating(t.song__pk),t.rating=this.rating,this.closeDialog("ratingDialog")},openRatingDialog:function(t){this.ratingDialog=!0,this.selected=t},openAddDialog:function(t){this.addDialog=!0,this.selected=t},closeDialog:function(t){this.$data[t]=!1}},mounted:function(){this.$http.defaults.xsrfHeaderName="X-CSRFToken",this.$http.defaults.xsrfCookieName="csrftoken"}}),s=i,o=(n("7114"),n("2877")),c=Object(o["a"])(s,a,r,!1,null,null,null);e["a"]=c.exports},7114:function(t,e,n){"use strict";n("1fcb")},"84af":function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-parallax",{class:t.styles,attrs:{dark:"",src:t.image,height:t.height}},[n("div",{staticClass:"bannertext-background"},[n("h1",{staticClass:"banner-header text-h4 font-weight-thin mb-4 text-center"},[t._v(" "+t._s(t.heading)+" ")]),n("h4",{staticClass:"subheading text-center"},[t._v(" "+t._s(t.subheader)+" ")])])])},r=[],i={name:"Banner",props:{styles:{type:String},image:{type:String},height:{type:String},heading:{type:String},subheader:{type:String}},data:function(){return{}}},s=i,o=(n("3178"),n("2877")),c=Object(o["a"])(s,a,r,!1,null,"1525f886",null);e["a"]=c.exports},"864d":function(t,e,n){},"91b8":function(t,e,n){"use strict";n("cac7")},a763:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-card",[n("v-tabs",{staticClass:"d-flex justify-center",attrs:{"hide-slider":""}},[n("v-tab",{staticClass:"home",attrs:{href:"/"}},[t._v(" Home ")]),n("v-tab",{attrs:{href:"/anime"}},[t._v(" Anime ")]),n("v-tab",{attrs:{href:"/top"}},[t._v(" Top ")]),n("v-tab",{attrs:{href:"/random"}},[t._v(" Random ")]),n("form",{attrs:{id:"search",action:"/search"}},[n("v-text-field",{staticClass:"search mt-1",class:{closed:t.searchClosed&&!t.query},attrs:{id:"query",name:"q",type:"search",placeholder:"Search",filled:"",dense:"","prepend-inner-icon":"mdi-magnify"},on:{focus:function(e){t.searchClosed=!1},blur:function(e){t.searchClosed=!0}},model:{value:t.query,callback:function(e){t.query=e},expression:"query"}})],1)],1)],1)},r=[],i={name:"HomeAppBar",props:{},data:function(){return{searchClosed:!0,query:null}}},s=i,o=(n("497b"),n("2877")),c=Object(o["a"])(s,a,r,!1,null,null,null);e["a"]=c.exports},ae3a:function(t,e,n){"use strict";n("864d")},cac7:function(t,e,n){},d546:function(t,e,n){"use strict";var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-card",{attrs:{elevation:"0"}},[n("v-toolbar",{attrs:{flat:""}},[n("a",{attrs:{href:"/"}},[n("v-img",{attrs:{src:"/static/site-logo-trans.png","max-width":"267","max-height":"63"}})],1),n("v-spacer"),n("div",{staticClass:"d-flex justify-space-between"},[n("div",["AnonymousUser"!=t.user?n("a",{attrs:{href:"/profile/"+t.user}},[t._v(" "+t._s(t.user)+" "),n("v-icon",[t._v("mdi-account")])],1):n("a",{attrs:{href:"/auth/login"}},[t._v("Login")])]),n("br"),n("a",{attrs:{href:"/auth/logout"}},[n("v-icon",[t._v("mdi-exit-to-app")])],1)])],1)],1)},r=[],i={name:"Toolbar",props:{user:{type:String}}},s=i,o=(n("91b8"),n("2877")),c=Object(o["a"])(s,a,r,!1,null,"0f36f594",null);e["a"]=c.exports},dde9:function(t,e,n){},efaa:function(t,e,n){}});