import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-structual-directive',
	templateUrl: './structual-directive.component.html',
	styleUrls: ['./structual-directive.component.css']
})
export class StructualDirectiveComponent implements OnInit {

	public isClassEnable = false
	public isStyleEnable = false
	public age: number = 0
	public data: any[] = [
		{
			id: 1,
			name: 'iPhone',
			price: 120000
		}
	]

	public dataFromServer: any[] = [
		{
			id: 1,
			name: 'iPhone',
			price: 120000
		},
		{
			id: 2,
			name: 'SamSung',
			price: 100000
		},
		{
			id: 3,
			name: 'Oppo',
			price: 70000
		}
	]


	public products: string[] = ['Apple', 'Microsoft', 'SamSung', 'Huawei']

	constructor() { }

	ngOnInit() {
	}

	onLoadDataFromServer() {
		this.data = this.dataFromServer
	}

	myTrackByFunction(index, item) {
		return item.id
	}

	myNGClass(){
		return {
			'my-boder':this.isClassEnable,
			'my-color':this.isClassEnable
		}
	}

	myNGStyle(){
		return{
			'color': this.isStyleEnable ? 'red' : '',
			'border': this.isStyleEnable ? '1px solid green':''
		}
	}
}
