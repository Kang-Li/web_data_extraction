odoo.define('web_data_extraction', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');

var Dashboard = Widget.extend({
    template: 'WebDataExtractionMain',

    init: function(parent, data){
        return this._super.apply(this, arguments);
    },

    start: function(){
        return true;
    },


});



core.action_registry.add('web_data_extraction.main', Dashboard);

return {
    Dashboard: Dashboard,
};

});
