package com.softwareChaser.springboot.Repository;



import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.softwareChaser.springboot.Model.Question;




@Repository
public interface QuestionRepository extends JpaRepository<Question,Long> {


	
//
//	public  List<Question> findBySubjectAndLevel(Subject subject, String level);
	}
