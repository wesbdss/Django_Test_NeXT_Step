# Django_Test_NeXT_Step

 <p>Configurar o database postgres na configuração /myapi/settings</p>
 			<p>Rodar: pip install -t requirements.txt</p>
            <p>Rodar: python manage.py makemigrations</p>
            <p>Rodar: python manage.py migrate</p>
            <p>Configurar conta de admin com: python manage.py createsuperuser</p>
            <p>Rodar: python manage.py runserver</p>
            <p>Logar para ter acesso ao POST dos endpoints</p>
            <h2>Código utilizado nos Triggers Postegres</h2>
            <code>
CREATE OR REPLACE FUNCTION person_insert_t_fnc()
RETURNS trigger AS

$$
	BEGIN
		INSERT INTO "api_person_audit" ("person_id_id","person_audit_type","cpf_new","last_update")
		VALUES(NEW."id",1,NEW."cpf",current_date);
		RETURN NEW;
	END;	
$$
LANGUAGE 'plpgsql';



CREATE TRIGGER on_insert_person
AFTER INSERT 
on "api_person"
FOR EACH ROW
EXECUTE PROCEDURE person_insert_t_fnc();


CREATE OR REPLACE FUNCTION person_update_t_fnc()
RETURNS trigger AS

$$
	BEGIN
    IF OLD.cpf IS NOT DISTINCT FROM NEW.cpf THEN
		INSERT INTO "api_person_audit" ("person_id_id","person_audit_type","cpf_new","last_update")
		VALUES(NEW."id",2,NEW."cpf",current_date);
        END IF;

        IF OLD.cpf IS NOT DISTINCT FROM NEW.cpf THEN
            INSERT INTO "api_person_audit" ("person_id_id","person_audit_type","cpf_new","cpf_old","last_update")
            VALUES(NEW."id",2,NEW."cpf",OLD.cpf,current_date);
        END IF;
		
		RETURN NEW;
	END;	
$$

LANGUAGE 'plpgsql';

CREATE TRIGGER on_update_person
AFTER UPDATE 
on "api_person"
FOR EACH ROW
EXECUTE PROCEDURE person_update_t_fnc();
            </code>