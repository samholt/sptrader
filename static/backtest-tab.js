import React from 'react';
import {BacktestTable} from './tables/backtest-table';

var BacktestTab = React.createClass( {
    getInitialState: function() {
	return null;
    },
    render: function() {
	var info = this.props.info;
	var l = this;
	return (
		<div>
		{this.props.strategylist.map(function(s) {
		    return (<div key={s}><b>{s}</b><br/>
			    <BacktestTable
			    strategy={s}
			    data={l.props.data[s]}
			    header={l.props.headers[s]}
			    /></div>);
		})}
	    </div>);
    }
});

module.exports = BacktestTab;


