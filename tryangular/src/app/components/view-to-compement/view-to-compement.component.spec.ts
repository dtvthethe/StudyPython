import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewToCompementComponent } from './view-to-compement.component';

describe('ViewToCompementComponent', () => {
  let component: ViewToCompementComponent;
  let fixture: ComponentFixture<ViewToCompementComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewToCompementComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewToCompementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
