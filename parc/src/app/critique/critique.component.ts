import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { CritiqueService } from '../Service/critique.service';
import { CritiqueInterface } from '../Interface/critique.interface';

@Component({
  selector: 'app-critique',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatCardModule
  ],
  templateUrl: './critique.component.html',
  styleUrl: './critique.component.scss'
})
export class CritiqueComponent {
  public formulaireCritique: FormGroup;
  private attraction_id: number;

  constructor(
    private formBuilder: FormBuilder,
    private critiqueService: CritiqueService,
    private _snackBar: MatSnackBar,
    private route: ActivatedRoute,
    private router: Router
  ) {
    this.attraction_id = Number(this.route.snapshot.paramMap.get('id'));
    this.formulaireCritique = this.formBuilder.group({
      critique_id: [null],
      attraction_id: [this.attraction_id],
      nom: [''],
      prenom: [''],
      crit: ['', Validators.required],
      note: ['', [Validators.required, Validators.min(0), Validators.max(5)]],
    });
  }

  public onSubmit(): void {
    if (this.formulaireCritique.valid) {
      this.critiqueService.postCritique(this.formulaireCritique.value).subscribe({
        next: (response) => {
          this._snackBar.open(response.message, undefined, {
            duration: 2000
          });
          this.router.navigate(['/accueil']);
        },
        error: (error) => {
          console.log(error);
          this._snackBar.open('Erreur lors de l\'envoi de la critique', undefined, {
            duration: 2000
          });
        }
      });
    }
  }
}