import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-view-to-compement',
	templateUrl: './view-to-compement.component.html',
	styleUrls: ['./view-to-compement.component.css']
})
export class ViewToCompementComponent implements OnInit {

	public count: number = 0

	constructor() { }

	ngOnInit() {
	}

	onClick(event) {
		alert(event.target.innerText);
	}

	onDbClick(event) {
		alert(event.target.innerText);
	}

	onIncrement() {
		this.count++;
	}

}
