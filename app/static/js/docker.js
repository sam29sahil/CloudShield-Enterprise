/* =========================================
   Utility Classes
========================================= */

.shadow-hover:hover {

    box-shadow: 0 12px 30px rgba(0,0,0,.08);

}

.cursor-pointer {

    cursor: pointer;

}

.text-small {

    font-size: .9rem;

}

.rounded-xl {

    border-radius: 16px;

}


/* =========================================
   Responsive
========================================= */

@media (max-width:992px){

    .btn-group{

        display:flex;

        flex-wrap:wrap;

        gap:6px;

    }

    .table{

        font-size:.9rem;

    }

}

@media (max-width:768px){

    h2{

        font-size:1.5rem;

    }

    .card-body{

        padding:1rem;

    }

    .docker-terminal{

        font-size:12px;

    }

}

@media (max-width:576px){

    .table{

        font-size:.82rem;

    }

    .btn{

        font-size:.8rem;

    }

}