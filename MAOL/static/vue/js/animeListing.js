(function(e){function t(t){for(var r,o,c=t[0],i=t[1],l=t[2],f=0,p=[];f<c.length;f++)o=c[f],Object.prototype.hasOwnProperty.call(n,o)&&n[o]&&p.push(n[o][0]),n[o]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);u&&u(t);while(p.length)p.shift()();return s.push.apply(s,l||[]),a()}function a(){for(var e,t=0;t<s.length;t++){for(var a=s[t],r=!0,c=1;c<a.length;c++){var i=a[c];0!==n[i]&&(r=!1)}r&&(s.splice(t--,1),e=o(o.s=a[0]))}return e}var r={},n={animeListing:0},s=[];function o(t){if(r[t])return r[t].exports;var a=r[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,o),a.l=!0,a.exports}o.m=e,o.c=r,o.d=function(e,t,a){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(o.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(a,r,function(t){return e[t]}.bind(null,r));return a},o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="";var c=window["webpackJsonp"]=window["webpackJsonp"]||[],i=c.push.bind(c);c.push=t,c=c.slice();for(var l=0;l<c.length;l++)t(c[l]);var u=i;s.push([3,"chunk-vendors"]),a()})({1924:function(e,t,a){},3:function(e,t,a){e.exports=a("b63e")},"402c":function(e,t,a){"use strict";var r=a("a026"),n=a("ce5b"),s=a.n(n);a("bf40");r["default"].use(s.a);var o={};t["a"]=new s.a(o)},"497b":function(e,t,a){"use strict";a("efaa")},"91b8":function(e,t,a){"use strict";a("cac7")},a763:function(e,t,a){"use strict";var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-tabs",{staticClass:"d-flex justify-center"},[a("v-tabs-slider",{attrs:{color:"blue"}}),a("v-tab",[e._v(" Home ")]),a("v-tab",[e._v(" Anime ")]),a("v-tab",[e._v(" Top ")]),a("v-tab",[e._v(" Random ")]),a("v-text-field",{staticClass:"search mt-1",class:{closed:e.searchClosed&&!e.query},attrs:{placeholder:"Search",filled:"",dense:"","prepend-inner-icon":"mdi-magnify"},on:{focus:function(t){e.searchClosed=!1},blur:function(t){e.searchClosed=!0}},model:{value:e.query,callback:function(t){e.query=t},expression:"query"}})],1)},n=[],s={name:"HomeAppBar",props:{},data:function(){return{searchClosed:!0,query:null}}},o=s,c=(a("497b"),a("2877")),i=Object(c["a"])(o,r,n,!1,null,null,null);t["a"]=i.exports},a7a6:function(e,t,a){"use strict";var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-parallax",{attrs:{dark:"",src:"https://wallpaperboat.com/wp-content/uploads/2020/06/03/42361/aesthetic-anime-01.jpg"}},[a("v-row",{attrs:{align:"center",justify:"center"}},[a("v-col",{staticClass:"text-center",staticStyle:{color:"white"},attrs:{cols:"12"}},[a("div",{staticStyle:{"background-color":"rgba(128, 0, 128, 0.2)"}},[a("h1",{staticClass:"text-h4 font-weight-thin mb-4",staticStyle:{"text-shadow":"0 0 3px #FF0000, 0 0 5px #0000FF"}},[e._v(" MAOL ")]),a("h4",{staticClass:"subheading",staticStyle:{"text-shadow":"0 0 5px #800080"}},[e._v(" The best anime site since "+e._s(e.date.toLocaleString())+" ")])])])],1)],1)},n=[],s={name:"HomeBanner",data:function(){return{date:new Date(Date.now())}}},o=s,c=a("2877"),i=Object(c["a"])(o,r,n,!1,null,null,null);t["a"]=i.exports},b63e:function(e,t,a){"use strict";a.r(t);a("e260"),a("e6cf"),a("cca6"),a("a79d");var r=a("a026"),n=a("bc3a"),s=a.n(n),o=a("130e"),c=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("ToolBar",{attrs:{user:e.username}}),a("HomeAppBar"),a("HomeBanner"),a("v-card-title",[e._v(" Anime "),a("v-spacer"),a("v-text-field",{staticClass:"search mt-1",class:{closed:e.searchClosed&&!e.query},attrs:{placeholder:"Search",filled:"",dense:"","prepend-inner-icon":"mdi-magnify"},on:{focus:function(t){e.searchClosed=!1},blur:function(t){e.searchClosed=!0}},model:{value:e.search,callback:function(t){e.search=t},expression:"search"}})],1),a("v-data-table",{staticClass:"elevation-1",attrs:{headers:[{value:"cover"},{text:"Name",value:"english_name"}],items:e.animes,"items-per-page":10,search:e.search},scopedSlots:e._u([{key:"top",fn:function(){return[a("v-toolbar",{attrs:{flat:""}},[a("v-spacer")],1)]},proxy:!0},{key:"item.cover",fn:function(e){var t=e.item;return[a("v-img",{attrs:{contain:"","aspect-ratio":16/9,height:100,src:t.cover}})]}}])})],1)},i=[],l=a("d546"),u=a("a763"),f=a("a7a6"),p={name:"Listing",components:{ToolBar:l["a"],HomeAppBar:u["a"],HomeBanner:f["a"]},props:{animes:{type:Array},username:{type:String}},data:function(){return{search:"",searchClosed:!0}}},d=p,v=(a("f570"),a("2877")),h=Object(v["a"])(d,c,i,!1,null,null,null),m=h.exports,b=a("402c");r["default"].config.productionTip=!1,r["default"].use(o["a"],s.a),new r["default"]({vuetify:b["a"],el:"#list",components:{Listing:m}})},cac7:function(e,t,a){},d546:function(e,t,a){"use strict";var r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-card",{attrs:{elevation:"0"}},[a("v-toolbar",{attrs:{flat:""}},[a("a",{attrs:{href:"/"}},[a("v-img",{attrs:{src:"/static/site-logo-trans.png","max-width":"267","max-height":"63"}})],1),a("v-spacer"),a("div",{staticClass:"d-flex justify-space-between"},[a("div",["AnonymousUser"!=e.user?a("a",{attrs:{href:"/profile/"+e.user}},[e._v(" "+e._s(e.user)+" "),a("v-icon",[e._v("mdi-account")])],1):a("a",{attrs:{href:"/auth/login"}},[e._v("Login")])]),a("br"),a("a",{attrs:{href:"/auth/logout"}},[a("v-icon",[e._v("mdi-exit-to-app")])],1)])],1)],1)},n=[],s={name:"Toolbar",props:{user:{type:String}}},o=s,c=(a("91b8"),a("2877")),i=Object(c["a"])(o,r,n,!1,null,"0f36f594",null);t["a"]=i.exports},efaa:function(e,t,a){},f570:function(e,t,a){"use strict";a("1924")}});