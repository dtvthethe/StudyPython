import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-component-to-view',
	templateUrl: './component-to-view.component.html',
	styleUrls: ['./component-to-view.component.css']
})
export class ComponentToViewComponent implements OnInit {

	public name: string = 'DTVThe'
	public age: number = 24
	public isMarried:boolean = false
	public user: object = {
		name: 'Python',
		cl: 'Google'
	}

	public imgLink:string = 'https://s.vnecdn.net/vnexpress/restruct/i/v64/graphics/img_logo_vne_web.gif'
	public imgWidth:number = 200
	public imgAlt:string = 'VNExpress Logo'


	constructor() { }

	ngOnInit() {
	}

	showName() {
		return `Object: Name: ${this.user['name']}, ${this.user['cl']}`
	}

}
